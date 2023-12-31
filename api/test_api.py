# test_api.py

import requests
from .schemas import User

def test_create_user():
    user_data = {
        "username": "test",
        "email": "test@test.com",
        "password": "test",
    }
    response = requests.post("http://127.0.0.1:8000/users/", json=user_data)
    assert response.status_code == 200
    created_user = response.json()  # Haal de gemaakte gebruiker op uit de respons
    assert created_user["username"] == user_data["username"]
    assert created_user["email"] == user_data["email"]

    # Verifieer dat de response voldoet aan het Pydantic-model
    user_model = User(**created_user)
    assert user_model.username == user_data["username"]
    assert user_model.email == user_data["email"]

def test_read_kerstmarkten():
    response = requests.get("http://127.0.0.1:8000/kerstmarkten/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_kerstmarkt():
    response = requests.get("http://127.0.0.1:8000/kerstmarkten/1")
    assert response.status_code == 200
    assert "naam" in response.json()
    assert "locatie" in response.json()
    assert "datum" in response.json()

def test_read_kerstgerechten():
    response = requests.get("http://127.0.0.1:8000/kerstgerechten/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_kerstgerecht():
    response = requests.get("http://127.0.0.1:8000/kerstgerechten/1")
    assert response.status_code == 200
    assert "naam" in response.json()
    assert "beschrijving" in response.json()
    assert "prijs" in response.json()


def test_read_kerstdecoratie():
    response = requests.get("http://127.0.0.1:8000/kerstdecoratie/1")
    assert response.status_code == 200
    assert "naam" in response.json()
    assert "type" in response.json()
    assert "prijs" in response.json()

def test_read_kerstdecoraties():
    response = requests.get("http://127.0.0.1:8000/kerstdecoratie/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def get_auth_token(username: str, password: str):
    token_data = {
        "username": "test@test.com",
        "password": "test",
        "grant_type": "password",
        "scope": "openid",
        "client_id": "",
        "client_secret": "",
    }
    response = requests.post("http://127.0.0.1:8000/token", data=token_data)
    return response.json().get("access_token")




def test_create_kerstmarkt():
    kerstmarkt_data = {
        "id": 3,
        "naam": "Kerstmarkt 2023",
        "locatie": "Amsterdam",
        "datum": "2023-12-25",
    }
    response = requests.post("http://127.0.0.1:8000/kerstmarkten/", json=kerstmarkt_data)
    assert response.status_code == 401  # Ongeautoriseerd zonder token

    token = get_auth_token("test@test.com", "test")
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post("http://127.0.0.1:8000/kerstmarkten/", json=kerstmarkt_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["naam"] == kerstmarkt_data["naam"]
    assert response.json()["locatie"] == kerstmarkt_data["locatie"]
    assert response.json()["datum"] == kerstmarkt_data["datum"]

def test_create_kerstgerecht():
    kerstgerecht_data = {
        "id": 4,
        "naam": "Kerstgerecht 2023",
        "beschrijving": "Heerlijk kerstgerecht",
        "prijs": 19.99,
    }

    # Ongeautoriseerd verzoek moet falen
    response = requests.post("http://127.0.0.1:8000/kerstgerechten/", json=kerstgerecht_data)
    assert response.status_code == 401

    # Geautoriseerd verzoek moet slagen
    token = get_auth_token("test@test.com", "test")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post("http://127.0.0.1:8000/kerstgerechten/", json=kerstgerecht_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["naam"] == kerstgerecht_data["naam"]
    assert response.json()["beschrijving"] == kerstgerecht_data["beschrijving"]
    assert response.json()["prijs"] == kerstgerecht_data["prijs"]


def test_create_kerstdecoratie():
    kerstdecoratie_data = {
        "id": 3,
        "naam": "Kerstdecoratie 2023",
        "type": "type 3",
        "prijs": 29.99,
    }

    # Ongeautoriseerd verzoek moet falen
    response = requests.post("http://127.0.0.1:8000/kerstdecoratie/", json=kerstdecoratie_data)
    assert response.status_code == 401

    # Geautoriseerd verzoek moet slagen
    token = get_auth_token("test@test.com", "test")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post("http://127.0.0.1:8000/kerstdecoratie/", json=kerstdecoratie_data, headers=headers)
    print(response.status_code)
    print(response.content)
    assert response.status_code == 200
    assert response.json()["naam"] == kerstdecoratie_data["naam"]
    assert response.json()["type"] == kerstdecoratie_data["type"]
    assert response.json()["prijs"] == kerstdecoratie_data["prijs"]

def test_update_kerstmarkt():
    kerstmarkt_data = {
        "id": 1,
        "naam": "Updated Kerstmarkt",
        "locatie": "Rotterdam",
        "datum": "2023-12-26",
    }

    # Ongeautoriseerd verzoek moet falen
    response = requests.put("http://127.0.0.1:8000/kerstmarkten/1", json=kerstmarkt_data)
    assert response.status_code == 401

    # Geautoriseerd verzoek moet slagen
    token = get_auth_token("test@test.com", "test")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put("http://127.0.0.1:8000/kerstmarkten/1", json=kerstmarkt_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["naam"] == kerstmarkt_data["naam"]
    assert response.json()["locatie"] == kerstmarkt_data["locatie"]
    assert response.json()["datum"] == kerstmarkt_data["datum"]
