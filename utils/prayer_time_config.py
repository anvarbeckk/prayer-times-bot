import datetime
import requests

p_api = 'http://api.aladhan.com/v1/calendar/'


clock_api = datetime.datetime.now()

day_of_month = clock_api.strftime("%d")
days = int(day_of_month) - 1

clock = clock_api.strftime("%p")
