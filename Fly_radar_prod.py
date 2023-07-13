import requests
import json
import xml


api_key = 'a45028db-da11-4863-9dc6-162a7aed2a50'
endpoint = 'airlines'
base_url = 'https://airlabs.co/api/v9/'

# Код авиакомпании IATA, по которому вы хотите получить информацию
iata_code = ''

# Формирование URL-адреса запроса с добавлением ключа API и параметра iata_code
url = f"{base_url}{endpoint}?api_key={api_key}&iata_code={iata_code}"

response = requests.get(url)

if response.status_code == 200:
    # Получение данных об авиакомпании в формате JSON
    airline_data = response.json()
    sky_up_info = ""
    for i in airline_data['response']:
        if i['icao_code'] == "SQP":
            sky_up_info += str(i)
    print(sky_up_info)
    # for key in airline_data:
    #     value = airline_data[key]
    #     print(f"{key}: {value}")
    
    # Проверка наличия ключа 'name'
    if 'name' in airline_data:
        # Вывод информации об авиакомпании
        print(f"Название авиакомпании: {airline_data['name']}")
        print(f"Код IATA: {airline_data['iata_code']}")
        # Дополнительно можно выводить другие доступные данные об авиакомпании
    else:
        print("Данные об авиакомпании недоступны.")
else:
    print(f"Ошибка при выполнении запроса: {response.status_code} - {response.text}")