# Learn to use streamlit for building custom LLM interfaces

## Getting started

Requirements:

- Python >= 3.11 (will be installed by miniconda)
- [Miniconda](https://docs.anaconda.com/free/miniconda/)

### Install Miniconda

#### Windows

Open powershell and enter the following commands. (copy paste them)

```powershell
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S
del miniconda.exe
```

#### macOS

Open the Terminal and go for the first option for newer Apples with a M1 / M2 / M3 or newer processor and the second for older Intel based Macs.

Apple Silicon:

```shell
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

Intel:

```shell
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

### Linux

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

### Create an environment for `learn-streamlit`

Open a new Terminal (for all operating systems)


Get a copy of the repo 
```shell
git clone https://github.com/mi-skam/learn-streamlit
```

Create the environment, activate it and install the dependencies for [streamlit](https://streamlit.io/)
```shell
conda create -y -n learn-streamlit python=3.11
conda activate learn-streamlit
pip install -r requirements.txt
```

## Running streamlit applications

### Using conda

To leave the environment enter `conda deactivate` and to re-enter `conda activate learn-streamlit`, which is necessary everytime you open a Terminal / Shell as the environment is only ephemeral.

### Start an app

As the apps are API based, you need to get a [API key from OpenAI](https://platform.openai.com/api-keys). Make this key known to your environment like so (also in the Terminal):

Linux / macOS

```
export OPENAI_API_key="sk..." # change it with your key
```

Windows:

```powershell
$Env:OPENAI_API_KEY="sk..." # change it with your key
```

To run streamlit apps, you enter `streamlit run <app_name> (e.g. "1 - hello openai.py")`
