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
    metro_route += metro_station + ','

   array_index -= 1

 else:
  while metro_station != destination:
   metro_station = station_list[array_index]

   if metro_station == destination:
    metro_route += metro_station 

   else:
    metro_route += metro_station + ','

   array_index += 1

 return metro_route


source_metro_station = input('Enter onboarding metro station from above choices: ')
source_tag = input('Enter onboarding metro station tag from above choices: ')

destination_metro_station = input('Enter destination metro station: ')
destination_tag = input('Enter destination tag: ')

route = get_metro_route('{} - {}'.format(source_metro_station,source_tag),'{} - {}'.format(destination_metro_station,destination_tag))

print(route)

  

