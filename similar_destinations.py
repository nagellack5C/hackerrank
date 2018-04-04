#https://www.hackerrank.com/contests/booking-hackathon/challenges/similar-destinations

n_of_tags = int(input())
strings = []
while True:
    try:
        strings.append(input().split(":"))
    except(EOFError):
        break
destinations = {}
#print(strings)
for i in strings:
  city = i[0]
  tags = i[1].split(",")
  destinations[city] = tags
#print(destinations)

cities = list(destinations.keys())
#print(cities)

groups = []

no_new_groups = False
for city in cities:
  for compared_city in cities:
    if city != compared_city:
      tags = []
      for tag in destinations[compared_city]:
        if tag in destinations[city]:
          tags.append(tag)
      if len(tags) >= n_of_tags:
        was_in = False
        for group in groups:
          if set(tags) == set(group[1]):
            was_in = True
            if compared_city not in group[0]:
              group[0].append(compared_city)
            if city not in group[0]:
              group[0].append(city)
        if not was_in:
          groups.append([[city, compared_city], tags])
      break
    
print(groups)
