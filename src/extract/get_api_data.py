import requests
import datetime
import pprint


def get_flight():


    params = {
    'access_key': 'YOUR ACCESS KEY'
    }

    api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

    api_response = api_result.json()

    for flight in api_response["data"]:
        print("** Flight Details **")
        for key, value in flight.items():
            pprint.pprint(f"{key}: {value}")
        print("--------------------")

def get_flights(flight_date):
    # Replace 'YOUR_ACCESS_KEY' with your actual access key
    params = {
        'access_key': access_key,
        'flight_date': flight_date
    }

    api_result = requests.get('https://api.aviationstack.com/v1/flights', params=params)
    api_response = api_result.json()

    if api_response.get("data"):
        for flight in api_response["data"]:
            print("** Flight Details **")
            for key, value in flight.items():
                print(f"{key}: {value}")
            print("--------------------")
    else:
        print(f"No flights found for the date: {flight_date}")

# Example usage
flight_date = '2024-03-15'  # Replace with your desired date in YYYY-MM-DD format
get_flights(flight_date)
