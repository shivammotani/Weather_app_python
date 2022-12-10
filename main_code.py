import pandas as pd
import requests
import json
import datetime

# Function to get response in Json Format
def get_response_json(city, date,api_key,base_url):
    req = requests.get(base_url,
        params={'param':['temperature'],
        'start':date,
        'end':date,
        'location':city,
        'freq':'D',
        'api-key' : api_key}
        )
    return req.json()
    
# Function to fetch Temperature from the response received through API 
def convert_to_tabular_and_ret_temp(response):
    weather_data = json.loads(response['data'])
    df = pd.DataFrame(index=pd.to_datetime(weather_data['index'],
                                       unit='s'),
                  data=weather_data['data'],
                  columns=weather_data['columns'])
    return (df.iloc[0,4])

## Code Starts here

print("Enter City Name")
city = input()
print("Enter Date in YYYY-MM-DD format")
date = input()
## Replace the below AP_KEY with your own key
api_key = 'b504c6776a1943a5a65e865bbf4ed764'
base_url = 'https://api.oikolab.com/weather'

req = get_response_json(city, date,api_key,base_url)

temp = convert_to_tabular_and_ret_temp(req)

print(f"Temperature for {city} on {date} is {temp} ^C")

