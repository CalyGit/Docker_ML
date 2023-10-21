# Sepsis Risk Prediction
Develop a Machine Learning API (Application Programming Interface) using FastAPI.

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![MIT licensed](https://img.shields.io/badge/license-mit-blue?style=for-the-badge&logo=appveyor)](./LICENSE)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white%29)

## Introduction

Welcome to the Sepsis Risk Prediction project! This repository hosts an application powered by FastAPI ,scikit-learn and Docker that predicts the probability of a patient having sepsis based on their vital signs and medical data.

![API illustration](/Images/API%20interface.jpg)

**Image** : *Sepsis Prediction api - screenshot*

## Project Overview
In the healthcare industry, early detection of sepsis can be a matter of life and death. This project aims to provide a tool that can assist healthcare professionals in identifying patients at risk of sepsis by analyzing their vital signs and other medical data. The project combines the power of machine learning and a user-friendly web interface to streamline the prediction process.

## Key Features
- **Predictive Model**: Utilizes a pre-trained machine learning model to predict the likelihood of sepsis based on patient data.
- **FastAPI Web Interface**: Provides a user-friendly web interface to input patient data and receive predictions.
- **Confidence Scoring**: Calculates a confidence score for predictions, aiding in the decision-making process.
- **Easy Deployment**: You can easily deploy this application in a Docker container for practical use in healthcare settings.

## Setup

Install the required packages to be able to run the evaluation locally.

You need to have [`Python 3`](https://www.python.org/) on your system (**a Python version lower than 3.10**). Then you can clone this repo and being at the repo's `root :: repository_name> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The both long command-lines have a same structure, they pipe multiple commands using the symbol ` ; ` but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## Run FastAPI

- Run the app (being at the repository root):
        
  FastAPI:
    
    

          uvicorn src.main:app --reload 




  - Go to your browser at the following address, to explore the api's documentation and try out the API :
        
      http://127.0.0.1:8000/docs

## Run Dockerized app

To run the Dockerized FASTAPI application, follow these steps:

1. Build the Docker image from the project's root directory:
    ```
    docker build -t sepsis-prediction-app .
    ```

2. Run the Docker container:
    ```
    docker run -p 7860:7860 sepsis-prediction-app
    ```
## Deploying Your App on Hugging Face Spaces
To deploy your Dockerized FASTAPI app on Hugging Face Spaces, follow these steps:

1. Create a new Space in your Hugging Face Spaces account.
2. Upload your files(Dockerfile, main.py, requirements.txt, pipeline.pkl).
3. Wait as Hugging Face Spaces builds your app automatically after you have uploaded the files.
4. Access your deployed app using the provided URL.

Congratulations! You have successfully deployed your app on Hugging Face Spaces.

## Deployed App 
Check out this [example](https://calistus-sepsis-prediction-app.hf.space/docs) of a deployed app on Hugging Face Spaces.


## Screenshots

_API Interface_
![API Interface](/Images/API%20interface.jpg)

_Execution Interface_
![Execution Interface](/Images/execution%20.jpg)



## Contributing

This repo is open for contributions. Feel free to make a Pull Request or report an issue 😃.

Please do not forget to put a description when you make your PR 🙂.

## Medium Article
[![Calistus Saratuki Medium](https://github-readme-medium.vercel.app/?username=@calistussaratuki)](https://calistussaratuki.medium.com/sepsis-prediction-api-with-fastapi-and-docker-f92148d58c55)
## Author
![Twitter Follow](https://img.shields.io/twitter/follow/the1_caly)

