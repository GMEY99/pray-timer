import requests

def praying_time():
     city=input('Enter city name: ').lower()
     country=input('Enter country name: ').lower()
     year=input('Enter year: ')
     month=input('Enter month: ')
     url = f'http://api.aladhan.com/v1/calendarByCity/{year}/{month}?city={city}&country={country}&method=2'
     response = requests.get(url)
     # dd=response.content
     datax = response.json()
     # Move the print statement before the return if you want to see the data
     x = datax["data"][0]
     y=x["timings"].items()
     z=[]
     for key, value in y:
          print(f'{key} : {value.strip('(EEST)')}')
     # print(dd)
praying_time()

