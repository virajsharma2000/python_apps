import requests

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
    

source_metro_station = input('Enter onboarding metro station: ')
destination_metro_station = input('Enter destination metro station: ')

route = get_metro_route(source_metro_station,destination_metro_station)

print(route)
