import json
import math

def lambda_handler(event, context):
    # Check if there are query string parameters
    if 'queryStringParameters' not in event or event['queryStringParameters'] is None:
        # Return welcome message in an HTTP response
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/plain"
            },
            "body": "Welcome to the Prime Factors Calculator! Please pass in a number as a query string parameter."
        }
    else:
        # Get the number from the URL parameter
        number = int(event['queryStringParameters']['number'])

        # Calculate the prime factors
        factors = prime_factors(number)

        # Return the factors in an HTTP response
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"factors": factors})
        }

    return response

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors
