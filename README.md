# Spamapi - Spam Detection API

## Overview
This project is a simple spam detection API built using Heroku, FastAPI, Pydantic, and Uvicorn. The API utilizes a machine learning model developed by me to detect whether a given comment or message is spam or not.

## Features
Spam Detection: The API can classify input text as spam or ham (normal) based on the trained machine learning model.
Easy Integration: The API is designed to be easily integrated into other applications or services through simple HTTP requests.
Scalability: Hosted on Heroku, the API can easily handle multiple requests and is scalable to accommodate increased traffic.

## Usage 

```python
import requests

# Define the API endpoint and payload
url = 'https://protected-brushlands-74008-9a69381fe196.herokuapp.com/' # Here is the endpoint
params = {
    "Comment": "Congratulations! You've won a free cruise vacation! Click this link to claim your prize now!"
}

# Send request to the API endpoint
response = requests.post(url, json=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response from the API
    print("API Response:")
    print(response.json())
else:
    # Print an error message if the request failed
    print("Error:", response.status_code)
```

## Technologies
Project is created with:
* scikit-learn
* pandas
* FastAPI
* uvicorn
* Heroku
* Pydantic
