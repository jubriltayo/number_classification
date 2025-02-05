from fastapi import FastAPI, Request
import httpx


app  = FastAPI()

# Fetch fun fact about a number asynchronously
async def get_fun_fact(number: int) -> str:
    url = f"http://numbersapi.com/{number}/math"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "No fact available"


# Check if a number is prime
def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Check if a number is perfect
def is_perfect(number: int) -> bool:
    total = sum(i for i in range(1, number) if number % i == 0)
    return total == number

# Check if a number is an Armstrong number
def is_armstrong(number: int) -> bool:
    digits = str(number)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == number

# Calculate digit sum
def digit_sum(number: int) -> int:
    return sum(int(d) for d in str(number))

# Determine properties of a number
def classify_number_properties(number: int):
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")
    return properties

# Generate formatted fun fact if Armstrong number
def format_fun_fact(number: int) -> str:
    if is_armstrong(number):
        digits = [int(d) for d in str(number)]
        formatted_fact = f"{number} is an Armstrong number because " + " + ".join(
            [f"{d}^{len(digits)}" for d in digits]
        ) + f" = {number}"
        return formatted_fact
    return None
    


# API endpoint to get fun fact about a number
@app.get("/api/classify-number")
async def classify_number(request: Request):
    number_param = request.query_params.get("number")

    if not number_param or not number_param.isdigit():
        return {
            "number": number_param,
            "error": True
        }
    
    number = int(number_param)
    fun_fact = format_fun_fact(number) or await get_fun_fact(number)    
    
    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": classify_number_properties(number),
        "digit_sum": digit_sum(number), 
        "fun_fact": fun_fact
    }
