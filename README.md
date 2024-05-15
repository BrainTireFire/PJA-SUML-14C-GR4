# PJA-SUML-14C-GR4

## Getting started

### Creating a Miniconda Environment
1.	Download Miniconda from the official website.
2.	Run the script create_env_conda.ps1 in Anaconda PowerShell Prompt (type ./create_env_conda.ps1 when located in the conf directory). Before running, make sure the environments.yml file exists. This file contains the necessary data to install required packages in the environment.

### Running the Main Script main.py
1. To create, train, prepare, and save the model, run the script main.py.
2. main.py executes sub-modules located in the "modules" folder.
3. Sub-modules are responsible for creating, evaluating the model, downloading the dataset, etc.
