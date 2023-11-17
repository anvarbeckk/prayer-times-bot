from .prayer_time_config import p_api, days
import requests


def primary(city):
    p_url = f"{p_api}={city}&"
    response = requests.get(p_url)
    h_one  = response.json()
    h_two = h_one.get('data')[days]['timings']

    today = h_one.get('data')[days]['date']['readable']

    return f"<b>{h_one.get('data')[days]['date']['hijri']['date']}</b>\n\nHere are your prayer times for today:\n\n<code>Fajr:     {h_two['Fajr'][0:5]}\nDhuhr:    {h_two['Dhuhr'][0:5]}\nAsr:      {h_two['Asr'][0:5]}\nMaghrib:  {h_two['Maghrib'][0:5]}\nIsha:     {h_two['Isha'][0:5]}</code>"