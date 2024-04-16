import streamlit as st

st.header("st.button")

if st.button("Say hello"):
    st.write("Why hello?")
else:
    st.write("Goodbye")
