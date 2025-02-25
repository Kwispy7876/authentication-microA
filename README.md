# User Registration/Authentication Microservice
This microservice handles user authentication, including **user registration** and **user login**, using **ZeroMQ** for communication. 

## **Communication Contract**
The microservice listens on `tcp://localhost:5555` and expects **JSON-formatted requests** sent over a **ZeroMQ REQ-REP (request-reply) socket**. The response is always a JSON-formatted string.

### **How to Request Data**
To send a request to the authentication microservice, establish a ZeroMQ request socket and send a JSON object with the following format:

```json
{
    "action": "register", // or "login"
    "email": "user@example.com",
    "password": "SecurePass123!"
}

