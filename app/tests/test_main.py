from fastapi.testclient import TestClient
from app.main import app
import random
import string

client = TestClient(app)

def generate_user_name(length=8):
    characters = string.ascii_letters + string.digits  # Uppercase, lowercase letters, and digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def test_create_user():
    username = generate_user_name();
    response = client.post("/users/", json={"name": username, "email": username + "@example.com"})
    print(username)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["name"] == username

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200

def test_audit_logs():
    response = client.get("/audit/")
    assert response.status_code == 200

