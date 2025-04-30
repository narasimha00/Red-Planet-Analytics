
# data_fetcher.py
import requests

API_URL = 'https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0'

def fetch_data():
    print('Fetching api json data...')
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError('Failed to fetch data from NASA API.')
