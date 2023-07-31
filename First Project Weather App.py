
import requests


class City:
    def __init__(self,name,latitude, longitude, units = "metric") -> None:
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.units = units
        self.get_data()
    
    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.latitude}&lon={self.longitude}&appid=d8ee3e12a731cc056c63c2f2c9350e71")
            
        except:
            print ("You have connection error")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.min_temp = self.response_json["main"]["temp_min"]
        self.max_temp = self.response_json["main"]["temp_max"]

    def temp_print(self):
            if self.units == 'metric':

                print(f"In {self.name} temperature in celsius is {self.temp} with minimum temp as {self.min_temp} and max as {self.max_temp}")
            if self.units == 'imperial':
                print(f"In {self.name} temperature in Fahrenhiet is {self.temp} with minimum temp as {self.min_temp} and max as {self.max_temp}")


my_city = City('Tokyo',44.34, 10.99,'imperial')
my_city.temp_print()

my_city1 = City('Toronto',43.65, 79.38)
my_city1.temp_print()

#
# https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=d8ee3e12a731cc056c63c2f2c9350e71
