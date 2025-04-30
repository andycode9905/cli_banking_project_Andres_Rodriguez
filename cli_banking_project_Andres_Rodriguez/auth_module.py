# auth_module.py
# Handles user authentication and registration using password hashing and JSON file storage.
# Author: Andres Felipe Rodriguez Ortiz

import hashlib
from storage import load_json, save_json

# Path to the JSON file where user credentials are stored
USERS_FILE = "data/users.json"

def hash_password(password):
    """
    Converts a plain text password into a SHA-256 hash for secure storage.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    """
    Registers a new user by asking for a username and password.
    Stores the username and hashed password in users.json.
    """
    users = load_json(USERS_FILE)
    username = input("Enter a new username: ").strip()

    # Check if the username is already taken
    if any(u['username'] == username for u in users):
        print("Username already exists.")
        return

    password = input("Enter a password: ").strip()
    hashed_pw = hash_password(password)

    # Append the new user to the user list and save it
    users.append({
        "username": username,
        "password": hashed_pw
    })

    save_json(USERS_FILE, users)
    print("User registered successfully!")

def login_user():
    """
    Authenticates a user by checking entered credentials against stored data.
    Returns the user dict if login is successful, otherwise returns None.
    """
    users = load_json(USERS_FILE)
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    hashed_pw = hash_password(password)

    # Search for matching user credentials
    for user in users:
        if user["username"] == username and user["password"] == hashed_pw:
            return user

    # If no match found, login fails
    print("Invalid credentials.")
    return None

