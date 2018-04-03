import math
from operator import itemgetter

#consts
FOOT = 5/60
BIKE = 15/60
METRO = 20/60

#functions
def distance_between(point1lat, point1lon, point2lat, point2lon):
  EARTH_RADIUS = 6371; #in km
  point1_lat_in_radians  = math.radians( point1lat )
  point2_lat_in_radians  = math.radians( point2lat )
  point1_long_in_radians  = math.radians( point1lon )
  point2_long_in_radians  = math.radians( point2lon )

  return math.acos( math.sin( point1_lat_in_radians ) * math.sin( point2_lat_in_radians ) +
                 math.cos( point1_lat_in_radians ) * math.cos( point2_lat_in_radians ) *
                 math.cos( point2_long_in_radians - point1_long_in_radians) ) * EARTH_RADIUS

print(distance_between(48.844783, 2.357027, 48.838296, 2.322800))
print(distance_between(48.858949, 2.339843, 48.838296, 2.322800))
#read all data

#read destinations
number_of_destinations = int(input())
destinations = {}
for i in range(number_of_destinations):
  dest = input().split(" ")
  destinations[int(dest[0])] = [float(dest[1]), float(dest[2])]
#print(destinations)

#read tourist data
number_of_guests = int(input())
guests = []
for i in range(number_of_guests):
  guest = input().split(" ")
  guests.append([float(guest[0]), float(guest[1]), guest[2], int(guest[3])])
#print(guests)

#now on to work

result = []

for i in guests:
  max_distance = 0
  if i[2] == "foot":
    max_distance = FOOT*i[3]
  if i[2] == "bike":
    max_distance = BIKE*i[3]
  if i[2] == "metro":
    max_distance = METRO*i[3]
  #print(max_distance)
  #print(i)
  reachable = []
  for j in destinations:
    #print(destinations[j])
    dist = distance_between(destinations[j][0], destinations[j][1], i[0], i[1])
    if dist <= max_distance:
      reachable.append([j, dist])
  result.append(reachable)

for i in result:
  x = sorted(i, key=itemgetter(1, 0))
  y = []
  for j in range(len(x)):
    y.append(str(x[j][0]))
  print(" ".join(y))
