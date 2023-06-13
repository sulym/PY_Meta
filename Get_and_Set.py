class GlassofWather:
    def __init__(self, temperature) -> None:
        self.temperature = temperature

    @property
    def temperature(self):
        print("Get temperature")
        return self._temperature
    
    @temperature.setter
    def temperature(self, temperature: int):
        print("Set temperature")
        if not (0 <= temperature <= 100):
            print("Temperature in range 0 - 100")
            return
        self._temperature = temperature


new_temp = GlassofWather(25)
new_temp.temperature = 1000
print(new_temp.temperature)

