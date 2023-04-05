months = {'Jun': 18, 'Jul': 23.8, 'Aug': 22.9}
temperature = 20


def average_temperature(months: dict, temperature: int) -> dict:
    # write your code here
    return {k: v for k, v in months.items() if temperature < v}



print(average_temperature(months, temperature))