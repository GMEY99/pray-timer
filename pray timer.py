import requests

def praying_time():
     city=input('Enter city name: ').lower()
     country=input('Enter country name: ').lower()
     year=int(input('Enter year: '))
     month=int(input('Enter month: '))
     url = f'http://api.aladhan.com/v1/calendarByCity/{year}/{month}?city={city}&country={country}&method=2'
     response = requests.get(url)
     datax = response.json()
     x = datax["data"][0]
     y=x["timings"].items()
     z=[]
     for key, value in y:
          print(f'{key} : {value.strip('(EEST)')}')

