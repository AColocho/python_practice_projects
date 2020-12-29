import pyttsx3
import requests as r

# Get API key @ https://www.weatherapi.com

class morning:
    def __init__(self,API_key,zip):
        self.API_key = API_key
        self.zip = zip
        self.voice_engine = pyttsx3.init()
    
    def get_info(self):
        weather = 'http://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=1'.format(self.API_key,self.zip)
        weather_json = r.get(weather).json()
        
        condition = weather_json['current']['condition']['text']
        temperature = weather_json['current']['temp_f']
        feels_like = weather_json['current']['feelslike_f']
        forecast_max = weather_json['forecast']['forecastday'][0]['day']['maxtemp_f']
        forecast_min = weather_json['forecast']['forecastday'][0]['day']['mintemp_f']
        sunset = weather_json['forecast']['forecastday'][0]['astro']['sunset']
        alert = weather_json['alert']
        
        if len(alert) > 0:
            alert = weather_json['alert']['headline']
        else:
            alert = 0
        
        self.condition = condition
        self.temperature = temperature
        self.feels_like = feels_like
        self.forecast_max = forecast_max
        self.forecas_min = forecast_min
        self.sunset = sunset
        self.alert = alert
        
        
    def generate_sentence(self):
        if self.alert == 0:
            sentence = (f"Good morning! It's {self.condition}, the temperature is {self.temperature} degrees, but it feels like {self.feels_like} degrees. "
                        + f"The maximum temperature will be {self.forecast_max} degrees, and the minimum will be {self.forecas_min} degrees. "
                        + f"Sunset will be at {self.sunset}.")
        else:
            sentence = (f"Good morning! It's {self.condition}, the temperature is {self.temperature} degrees, but it feels like {self.feels_like} degrees. "
                        + f"The following weather alert was issued {self.alert}. "
                        + f"The maximum temperature will be {self.forecast_max} degrees, and the minimum will be {self.forecas_min} degrees. "
                        + f"Sunset will be at {self.sunset}.")
        
        self.sentence = sentence
    
    def speak(self):
        self.voice_engine.say(self.sentence)
        self.voice_engine.runAndWait()
 

if __name__ == '__main__':
    morning = morning("API KEY","ZIPCODE")
    morning.get_info()
    morning.generate_sentence()
    morning.speak()