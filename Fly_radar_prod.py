
from datetime import datetime
import requests

aircraft_info_list = [
    "UR-SQA",
    "UR-SQC",
    "UR-SQF",
    "UR-SQB",
    "UR-SQG",
    "UR-SQH",
    "UR-SQQ",
    "UR-SQO",
    "UR-SQM",
    "UR-SQD",
    "UR-SQE"
    ]

# Запрос
def respons_flights(adress_url: str) -> list:
    response = requests.get(url)

    # Проверка условия статуса сервера 200 - ОК
    if response.status_code == 200:
        data_json_information = response.json()
    # Создание списка рейсов в полёте
    real_time_flights = []
    for flight in data_json_information["response"]:
        try:
            flight["reg_number"]
            if flight["reg_number"] in aircraft_info_list or flight["reg_number"] == "UR-SQP":
                for _ in flight:
                    reg_number = flight.get("reg_number", "N/A")
                    dep_iata = flight.get("dep_iata", "N/A")
                    arr_iata = flight.get("arr_iata", "N/A")
                    status = flight.get("status", "N/A")
                    alt = flight.get("alt", "N/A")

                real_time_flights.append(
                    [
                    f"Registration Number: {reg_number}",
                    f"Departure: {dep_iata}",
                    f"Arrival: {arr_iata}",
                    f"Status: {status}",
                    f"Alt. : {alt}"
                    ]
                    )
        except KeyError:
            continue
        
    return real_time_flights


api_key = 'a45028db-da11-4863-9dc6-162a7aed2a50'
endpoint = 'flights'
base_url = 'https://airlabs.co/api/v9/'

# Код авиакомпании IATA, по которому вы хотите получить информацию
iata_code = ''

# Формирование URL-адреса запроса с добавлением ключа API и параметра iata_code
url = f"{base_url}{endpoint}?api_key={api_key}&iata_code={iata_code}"
