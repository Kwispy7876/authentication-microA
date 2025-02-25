import zmq
import json

def send_request(action, email, password):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    
    request = {
        "action": action,
        "email": email,
        "password": password
    }
    
    socket.send_json(request)
    response = socket.recv_string()
    return response

if __name__ == "__main__":
    print("Testing User Authentication Microservice...")

    #********************** Test user registration **************************
    email = "testuser@example.com"
    password = "Password123!"
    print("Registering user:", send_request("register", email, password))


    #********************** Test successful login ***************************
    print("Logging in with correct credentials:", send_request("login", email, password))


    #********************* Test unsuccessful login **************************
    print("Logging in with incorrect password:", send_request("login", email, "WrongPassword"))
    

    #**************** Test login with non existent user *********************
    print("Logging in with non-existent user:", send_request("login", "fakeuser@example.com", "password"))


    #******************** Test registering another user *********************
    email2 = "anotheruser@example.com"
    password2 = "AnotherPass456!"
    print("Registering second user:", send_request("register", email2, password2))