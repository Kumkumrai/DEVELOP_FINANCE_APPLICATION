# tests/test_auth.py

import pytest
from app.auth import register, login

# Mock user data for testing
users = {}

def test_register():
    # Test successful registration
    register("john_doe", "password123")
    assert "john_doe" in users
    assert users["john_doe"] == "a91a1bdbe9a126c75f846a74e5b80cfde5b68ad0f3f443d0352d5e81f2954d92"  # Expected hashed password

    # Test registration failure with an existing username
    with pytest.raises(ValueError, match="Username already taken"):
        register("john_doe", "newpassword")

def test_login():
    # Test successful login
    register("jane_doe", "password123")
    login("jane_doe", "password123")  # This should pass without raising any exceptions

    # Test login failure with incorrect password
    with pytest.raises(ValueError, match="Incorrect password"):
        login("jane_doe", "wrongpassword")

    # Test login failure for non-existent user
    with pytest.raises(ValueError, match="User not found"):
        login("non_existent_user", "password")
