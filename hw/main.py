import pytest
from users import User

@pytest.fixture
def user_data():
    return {"name": "John", "id": 1, "level": 3}

@pytest.fixture
def user():
    return User()

def test_create_user(user, user_data):
    user.create_user(user_data["name"], user_data["id"], user_data["level"])
    assert user.get_user(user_data["id"]) == user_data

def test_update_user(user, user_data):
    user.create_user(user_data["name"], user_data["id"], user_data["level"])
    updated_data = {"name": "Jane", "id": 1, "level": 4}
    user.update_user(user_data["id"], updated_data)
    assert user.get_user(user_data["id"]) == updated_data

def test_delete_user(user, user_data):
    user.create_user(user_data["name"], user_data["id"], user_data["level"])
    user.delete_user(user_data["id"])
    assert user.get_user(user_data["id"]) is None

def test_get_user_not_found(user):
    assert user.get_user(999) is None

def test_get_all_users(user):
    user.create_user("Alice", 2, 2)
    user.create_user("Bob", 3, 1)
    assert len(user.get_all_users()) == 2

def test_high_level_users(user):
    user.create_user("Alice", 2, 2)
    user.create_user("Bob", 3, 1)
    user.create_user("Eve", 4, 3)
    assert len(user.get_high_level_users()) == 1
