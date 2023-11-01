def get_metro_route(source,destination):
 metro_station_list = open('metro_station_list','r').read()

 station_list = metro_station_list.split('\n')
 
 metro_station = source
 array_index = station_list.index(source)
 metro_route = ''

 if station_list.index(source) > station_list.index(destination):
  while metro_station != destination:
   metro_station = station_list[array_index]

   if metro_station == destination:
    metro_route += metro_station

   else:
    metro_route += metro_station + '<-'

   array_index -= 1

 else:
  while metro_station != destination:
   metro_station = station_list[array_index]

   if metro_station == destination:
    metro_route += metro_station 

   else:
    metro_route += metro_station + '->'

   array_index += 1

 return metro_route

def get_tag_by_metro_station(tag):
 metro_stations_and_tags = open('metro_stations_and_tags','r').read()

 for metro_stations in metro_stations_and_tags.split('\n'):
    if metro_stations.split(' - ')[0] == tag:
        metro_station = metro_stations.split(' - ')[1]

        return metro_station

    else:
        continue
    

source_metro_station = input('Enter onboarding metro station: ')
destination_metro_station = input('Enter destination metro station: ')

source_tag = input('Enter onboarding metro station tag: ')
destination_tag = input('Enter destination metro station tag: ')

route = get_metro_route(source_metro_station,destination_metro_station)

if source_tag == get_tag_by_metro_station(source_metro_station) and destination_tag == get_tag_by_metro_station(destination_metro_station):
    print(route)

else:
    print('I found the route but I will not show you the route I found because the entered tag of destination metro station or source metro station is incorrect')
