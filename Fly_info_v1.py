import requests
import json


def flight_info():
    url = "https://airlabs.co/api/v9/flights?flag=UA&api_key=a45028db-da11-4863-9dc6-162a7aed2a50"
    response = requests.get(url)
    flights_skyup = ''
    flight = ''
    if response.status_code == 200:
        airline_data = response.json()
        # print(airline_data['response'])
        for i in airline_data['response']:
            
            # if i['airline_iata']:
            #     print(i)
            if i['reg_number'] == "UR-SQQ":
                flight = (f"Flight status: {str(i['status'])}"
                        f"\nFlight height: {str(i['alt'])}"
                        f"\nFlight speed: {str(i['speed'])}")
    return flight

if __name__ == '__main__':
    print(flight_info())