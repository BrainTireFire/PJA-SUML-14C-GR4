# PJA-SUML-14C-GR4 - FINISHED

## Description

AmIPhat is a web application designed to predict obesity levels based on user-provided data. The application ensures compatibility across all current devices by being accessible through the latest web browsers.

## Getting started

### Creating a Miniconda Environment

1. Download Miniconda from the official website.
2. Run the script create_env_conda.ps1 in Anaconda PowerShell Prompt (type ./create_env_conda.ps1 when located in the conf directory). Before running, make sure the environments.yml file exists. This file contains the necessary data to install required packages in the environment.

### Running the Main Script main.py

1. To create, train, prepare, and save the model, run the script main.py while located in Training folder.
2. main.py executes sub-modules located in the "modules" folder.
3. Sub-modules are responsible for creating, evaluating the model, downloading the dataset, etc.

## Deployment

### Training

#### Docker

##### BUILD:

While located in Training folder run: docker build -t training-app .

##### START:

docker run -v .:/app/models -v .:/app/dataset/obesity-levels training-app

Replace the "." before the ":" signs in -v tags to specify folders:

1. Where model will be saved
2. From where to load the csv data

### API

#### Docker (FASTAPI)

##### BUILD:

While located in API/fastapi folder run: docker build -t fastapi-app .

##### START:

docker run -d -p 8000:8000 --name pja-suml-14c-gr4 -e PORT=8000 -v .:/app/ml_model fastapi-app

Replace the "." before the ":" sign in -v tag to specify from where to load model.

#### Streamlit

In root directory run:
streamlit run .\API\streamlit\app.py
