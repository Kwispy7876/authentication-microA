import zmq
import json
import os
import hashlib
import hmac

# file to store user credentials
USER_DB = "users.json"

# initialize user database
def initialize_db():
    if not os.path.exists(USER_DB):
        with open(USER_DB, "w") as f:
            json.dump({}, f)

# function to hash passwords
def hash_password(password):
    secret_key = b"abcd12345"
    return hmac.new(secret_key, password.encode(), hashlib.sha256).hexdigest()

# function to register a user
def register_user(email, password):
    with open(USER_DB, "r") as f:
        users = json.load(f)
    
    if email in users:
        return "User already exists."
    
    users[email] = hash_password(password)
    with open(USER_DB, "w") as f:
        json.dump(users, f)
    return "Registration successful."


# function to authenticate a user
def login_user(email, password):
    with open(USER_DB, "r") as f:
        users = json.load(f)
    
    if email not in users:
        return "User not found."
    
    if users[email] == hash_password(password):
        return "Login successful."
    else:
        return "Incorrect password."

# ZeroMQ server to handle authentication requests
def authentication_server():
    initialize_db()
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    
    # delete line below when implementing
    print("Authentication microservice running...")
    
    while True:
        message = socket.recv_json()
        action = message.get("action")
        email = message.get("email")
        password = message.get("password")
        
        if action == "register":
            response = register_user(email, password)
        elif action == "login":
            response = login_user(email, password)
        else:
            response = "Invalid action."
        
        socket.send_string(response)

if __name__ == "__main__":
    authentication_server()