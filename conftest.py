import pytest
import allure
import requests
import json


@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    header = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=header, json=payload)
    token = response.json()["token"]
    return token
