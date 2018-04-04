#https://www.hackerrank.com/contests/booking-hackathon/challenges/travel-profiles/submissions/code/1306928657

from operator import itemgetter

#read hotels
n_of_hotels = int(input())
hotels = []
for i in range (n_of_hotels):
  hotel_string = input().split(" ")
  hotel = []
  hotel.append(int(hotel_string[0]))
  hotel.append(int(hotel_string[1]))
  hotel.append(len(hotel_string) - 2)
  for j in range (2, len(hotel_string)):
    hotel.append(hotel_string[j])
  hotels.append(hotel)
#print(hotels)

#read guests
n_of_guests = int(input())
guests = []
for i in range (n_of_guests):
  guests_string = input().split(" ")
  guest = []
  guest.append(int(guests_string[0]))
  for j in range(1, len(guests_string)):
    guest.append(guests_string[j])
  guests.append(guest)
#print(guests)

for i in guests:
  applicable = []
  for j in hotels:
    if j[1] <= i[0]:
      facs = len(i) - 1
      for k in range(2, len(j)):
        if j[k] in i:
          facs -= 1
      if facs == 0:
        applicable.append(j)
  #print(applicable)
  x = sorted(applicable, key=itemgetter(1, 2))
  x = sorted(x, key=itemgetter(2), reverse=True)
  #print(x)
  if len(x) > 0:
    y = []
    for i in x:
      y.append(str(i[0]))
    print(" ".join(y))
  else:
    print("")
