# Number Classification API

## Overview
The **Number Classification API** is a FastAPI-based backend service that classifies numbers based on mathematical properties and provides a fun fact about the number. It supports:

- Prime number detection
- Perfect number identification
- Armstrong number verification
- Odd/Even classification
- Digit sum calculation
- Fun fact retrieval from the Numbers API

## Features
✅ Accepts GET requests with a number parameter\
✅ Returns JSON responses in a structured format\
✅ Handles errors and invalid inputs gracefully\
✅ Uses asynchronous requests for fast API responses\
✅ Strictly follows the required API specifications

## Technologies Used
- **Python** (FastAPI)
- **httpx** (Asynchronous HTTP requests)
- **Uvicorn** (ASGI server for FastAPI)

## API Specification

### **Endpoint:**
```plaintext
GET /api/classify-number?number=<integer>
```

### **Request Example:**
```plaintext
GET http://127.0.0.1:8000/api/classify-number?number=371
```

### **Successful Response (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### **Error Response (400 Bad Request):**
```json
{
    "number": "abc",
    "error": true
}
```

## Running the API Locally

### **1. Clone the Repository:**
```sh
git clone https://github.com/jubriltayo/hngx-stage1-number-classification.git
```

### **2. Install Dependencies:**
```sh
pip install fastapi uvicorn httpx
```

### **3. Start the Server:**
```sh
uvicorn main:app --reload
```

### **4. Test the API:**
Visit in your browser or use `curl`:
```sh
curl "http://127.0.0.1:8000/api/classify-number?number=371"
```

## Deployment
This API was deployed on **Render** with CORS enabled for external access. Other platforms like **Vercel, AWS, or Heroku** could also be used. 

