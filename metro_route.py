import requests
import random

def get_metro_route(source,destination):
 route = ''
 
 response = requests.get('https://us-central1-delhimetroapi.cloudfunctions.net/route-get?from={}&to={}'.format(source,destination))

 json = response.json()

 for metro_station in json['path']:
  if metro_station in json['interchange']:
   route += metro_station + ' - ' + 'interchange' + '\n'

  else:
   route += metro_station  + '\n'

 return route

def get_station_list(letter):
 if letter == 'All Stations':
  metro_stations = ''
  
  response = requests.get('https://raw.githubusercontent.com/Mansehej/DelhiMetroAPI/master/StationList.txt')

  stations = response.text

  number = 0
  
  for station in stations.split('\n'):
   number += 1
   metro_stations += str(number) + '.' + station + '\n'

  return metro_stations

 else:
  metro_stations = ''
  
  response = requests.get('https://raw.githubusercontent.com/Mansehej/DelhiMetroAPI/master/StationList.txt')

  stations = response.text

  number = 0
  
  for station in stations.split('\n'):
   if station.startswith(letter):
    number += 1
    metro_stations += str(number) + '.' + station + '\n'

   else:
    continue

  return metro_stations

def get_time(source,destination):
 response = requests.get('https://us-central1-delhimetroapi.cloudfunctions.net/route-get?from={}&to={}'.format(source,destination))

 json = response.json()

 time = int(json['time'])

 return time

def get_distance(source,destination):
 response = requests.get('https://us-central1-delhimetroapi.cloudfunctions.net/route-get?from={}&to={}'.format(source,destination))

 json = response.json()

 distance = 45 * int(json['time']) / 60

 return distance

 
want_to_do = input('do you want to get station list or get metro route or get time or get distance: ')

if want_to_do == 'get time':
 source_metro_station = input('Enter onboarding metro station: ')
 destination_metro_station = input('Enter destination metro station: ')

 time = get_time(source_metro_station,destination_metro_station)

 print(time,'minutes')
 
if want_to_do == 'get metro route':
 source_metro_station = input('Enter onboarding metro station: ')
 destination_metro_station = input('Enter destination metro station: ')

 route = get_metro_route(source_metro_station,destination_metro_station)

 print()
 print(route)

if want_to_do == 'get station list':
 letter = input("type a letter which's stations you want to get or if you want to get all stations kjust type All Stations: ")

 metro_stations = get_station_list(letter)

 print()
 print(metro_stations)

if want_to_do == 'get distance':
 source = input('Enter source metro station: ')
 destination = input('Enter destination metro station: ')

 distance = get_distance(source,destination)

 print(distance,'km')
 
