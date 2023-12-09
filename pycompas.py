def get_compas_direction(source_coordinates,destination_coordinates):
 source_latitude = source_coordinates[0]
 source_longitude = source_coordinates[1]

 destination_latitude = destination_coordinates[0]
 destination_longitude = destination_coordinates[1]

 direction = ''

 if source_latitude > destination_latitude:
  direction += 'South'

 if source_latitude < destination_latitude:
  direction += 'North'

 if source_longitude > destination_longitude:
  direction += 'West'

 if source_longitude < destination_longitude:
  direction += 'East'

 return direction
