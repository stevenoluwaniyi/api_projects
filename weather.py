from datetime import datetime
import os
import pytz
import requests
import math

API_KEY = os.getenv('API_KEY')
print(API_KEY)

if not API_KEY:
	raise ValueError("No API KEY set for weather application")

API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')

def query_api(city):
	try:
		print(API_URL.format(city,API_KEY))
		data = requests.get(API_URL.format(city,API_KEY)).json()
		print("********______ I am data ", data)
	except Exception as exc:
		print(exc)
		data = None
	return data
