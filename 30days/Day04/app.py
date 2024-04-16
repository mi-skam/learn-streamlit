try:
  import google.colab
  ON_COLAB = True
except Exception:
  ON_COLAB = False

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime

data = {}

if not ON_COLAB:
  data['df_agg'] = pd.read_csv('./data/Aggregated_Metrics_By_Video.csv').iloc[1:,:]
  data['df_agg_sub'] = pd.read_csv('./data/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')
  data['df_comments'] = pd.read_csv('./data/All_Comments_Final.csv')
  data['df_time'] = pd.read_csv('./data/Video_Performance_Over_Time.csv')
else:
  data['df_agg'] = pd.read_csv_url('https://raw.githubusercontent.com/mi-skam/learn-streamlit/main/30days/Day04/data/Aggregated_Metrics_By_Video.csv').iloc[1:,:]
  data['df_agg_sub'] = pd.read_csv_url('https://raw.githubusercontent.com/mi-skam/learn-streamlit/main/30days/Day04/data/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')
  data['df_comments'] = pd.read_csv_url('https://raw.githubusercontent.com/mi-skam/learn-streamlit/main/30days/Day04/data/All_Comments_Final.csv')
  data['df_time'] = pd.read_csv_url('https://raw.githubusercontent.com/mi-skam/learn-streamlit/main/30days/Day04/data/Video_Performance_Over_Time.csv')

@st.cache_resource
def prepare_data():
  # load_data
  
  data['df_agg'].columns = ['Video','Video title','Video publish time','Comments added','Shares','Dislikes','Likes',
                       'Subscribers lost','Subscribers gained','RPM(USD)','CPM(USD)','Average % viewed','Average view duration',
                       'Views','Watch time (hours)','Subscribers','Your estimated revenue (USD)','Impressions','Impressions ctr(%)']
  data['df_agg']['Video publish time'] = pd.to_datetime(data['df_agg']['Video publish time'], format="mixed")
  data['df_agg']['Average view duration'] = data['df_agg']['Average view duration'].apply(lambda x: datetime.strptime(x,'%H:%M:%S'))
  data['df_agg']['Avg_duration_sec'] = data['df_agg']['Average view duration'].apply(lambda x: x.second + x.minute*60 + x.hour*3600)
  data['df_agg']['Engagement_ratio'] =  (data['df_agg']['Comments added'] + data['df_agg']['Shares'] + data['df_agg']['Dislikes'] + data['df_agg']['Likes']) /data['df_agg'].Views
  data['df_agg']['Views / sub gained'] = data['df_agg']['Views'] / data['df_agg']['Subscribers gained']
  data['df_agg'].sort_values('Video publish time', ascending = False, inplace = True)    
  data['df_time']['Date'] = pd.to_datetime(data['df_time']['Date'],format="mixed")
  
  return data['df_agg'], data['df_agg_sub'], data['df_comments'], data['df_time']

df_agg, df_agg_sub, df_comments, df_data = prepare_data()

sidebar = st.sidebar.selectbox("Aggregate or Individual Videos analysis", ("Aggregate", "Individual"))
