import requests

URL = "https://tues2022.proxy.beeceptor.com/my/api/test"

class ApiTemperature:
    def __init__(self):
        data = requests.post(URL).json()

        self.temperatures = []

        for i in data['data']:
            self.temperatures.append(i['temperature'])

    @staticmethod
    def min_temp():
        currentApi = ApiTemperature()
        return min(currentApi.temperatures)

    @staticmethod
    def max_temp():
        currentApi = ApiTemperature()
        return max(currentApi.temperatures)

    @staticmethod
    def avg_temp():
        currentApi = ApiTemperature()
        return sum(currentApi.temperatures) / len(currentApi.temperatures)
