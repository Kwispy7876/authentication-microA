# User Registration/Authentication Microservice
This microservice handles user authentication, including **user registration** and **user login**, using **ZeroMQ** for communication. 

## **Communication Contract**
The microservice listens on `tcp://localhost:5555` and expects **JSON-formatted requests** sent over a **ZeroMQ REQ-REP (request-reply) socket**. The response is always a JSON-formatted string.

### **How to REQUEST Data**
To send a request to the authentication microservice, establish a ZeroMQ request socket and send a JSON object with the following format:

```json
{
    "action": "register",
    "email": "user@example.com",
    "password": "SecurePass123!"
}
```
### **Example Call**

```python
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

    socket.send_json(request)        # Sending request to microservice
    response = socket.recv_string()  # Receiving response
    return response                  # Returning response from microservice

# Example: Registering a user
response = send_request("register", "testuser@example.com", "SecurePass123!")
print("Microservice Response:", response)
```

---

### **How to RECEIVE Data**
The microservice responds with a **JSON-formatted string** based on the request.

- **Successful Registration:**
  ```json
  "User registered successfully."
  ```
- **Duplicate Registration Attempt:**
  ```json
  "Error: User already exists."
  ```
- **Successful Login:**
  ```json
  "Login successful."
  ```
- **Failed Login (Wrong Password or Non-existent User):**
  ```json
  "Error: Invalid email or password."
  ```
  
### **Example Call**

```python
response = send_request("login", "testuser@example.com", "SecurePass123!")
print("Authentication Response:", response)
```

---

### **UML Sequence Diagram**
![Screenshot_10](https://github.com/user-attachments/assets/66b27451-aa91-4d89-a080-a7337394e70f)
