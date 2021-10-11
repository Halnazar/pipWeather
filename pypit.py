from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

city = input("Какой город вас интересует? : ")
owm = OWM('2537926bb4dc3eb904fe2fcdda974d9f')
mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(city)
w = observation.weather
temperature = w.temperature('celsius')['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
speed = w.wind()

print("В городе " + city + " сейчас температура: " + str(temperature) + " по Цельсию")
print("Также, в указоноом городе: " + w.detailed_status)
print("Облачность: " + str(w.clouds))
print("Влажность: " + str(w.humidity))
print("Скорость ветра: " + str(w.wind()['speed']))
