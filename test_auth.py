# test_auth.py
from auth import authenticate, register

def test_valid_login():
    assert authenticate("john", "pass123") == True

def test_invalid_password():
    assert authenticate("john", "wrongpass") == False

def test_unknown_user():
    assert authenticate("unknown", "pass123") == False

def test_register_user():
    assert register("newuser", "newpass") == True

def test_login_registered_user():
    assert authenticate("newuser", "newpass") == True
