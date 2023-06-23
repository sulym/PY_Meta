class SlowResponse(Exception):
    def __init__(self, name: str, response: int) -> None:
        self.name = name
        self.response = response
    
    def __str__(self) -> None:
        return f"Warning! {self.name} has a slow response of {self.response} ms."


class ExtraSlowResponse(SlowResponse):
    def __str__(self) -> None:
        return f"Alarm! {self.name} has a very slow response of {self.response} ms."


class DangerouslySlowResponse(ExtraSlowResponse):
    def __str__(self) -> None:
        return f"Nuclear power station is under the danger! {self.name} has a dangerously slow response of {self.response} ms."


def check_device_response(device: dict) -> None:
    name = device["name"]
    response = device["response"]

    if response > 100:
        raise DangerouslySlowResponse(name, response)
    elif response > 75:
        raise ExtraSlowResponse(name, response)
    elif response > 50:
        raise SlowResponse(name, response)


def check_station_devices(devices: list) -> None:
    exceeded_norm = False
    for device in devices:
        try:
            check_device_response(device)
        except DangerouslySlowResponse as e:
            print(str(e) + " We have a serious troubles!")
            exceeded_norm = True
        except ExtraSlowResponse as e:
            print(str(e) + " Needs to be repaired!")
            exceeded_norm = True
        except SlowResponse as e:
            print(str(e) + " Take attention!")
            exceeded_norm = True
        
    if not exceeded_norm:
        print("Responses of all devices does not exceed the norm.")

            
print(check_station_devices(devices=[{"name": "Polar crane", "response": 76}]))

### m ###

class SlowResponse(Exception):
    def __init__(self, name: str, response: int) -> None:
        self.name = name
        self.response = response

    def __str__(self) -> str:
        return (
            f"Warning! {self.name} has a slow response of {self.response} ms."
        )


class ExtraSlowResponse(SlowResponse):
    def __str__(self) -> str:
        return f"Alarm! {self.name} has a very slow response of {self.response} ms."


class DangerouslySlowResponse(ExtraSlowResponse):
    def __str__(self) -> str:
        return (
            f"Nuclear power station is under the danger! "
            f"{self.name} has a dangerously slow response of {self.response} ms."
        )


def check_device_response(device: dict) -> None:
    if device["response"] > 100:
        raise DangerouslySlowResponse(device["name"], device["response"])
    if device["response"] > 75:
        raise ExtraSlowResponse(device["name"], device["response"])
    if device["response"] > 50:
        raise SlowResponse(device["name"], device["response"])


def check_station_devices(devices: list) -> None:
    correct_count = 0
    for device in devices:
        try:
            check_device_response(device)
            correct_count += 1
        except DangerouslySlowResponse as e_info:
            print(e_info, "We have a serious troubles!")
        except ExtraSlowResponse as e_info:
            print(e_info, "Needs to be repaired!")
        except SlowResponse as e_info:
            print(e_info, "Take attention!")
    if correct_count == len(devices):
        print("Responses of all devices does not exceed the norm.")
