#https://www.hackerrank.com/contests/booking-hackathon/challenges/facilities-extraction

n_of_facilities = int(input())
facilities = []
for i in range(n_of_facilities):
    facilities.append(input())
facilities_lower = []
for i in facilities:
    facilities_lower.append(i.lower())
search_string = input().lower()
present = []
for i in range(len(facilities_lower)):
    if facilities_lower[i] in search_string:
        if facilities[i] not in present:
            present.append(facilities[i])
print("\n".join(sorted(present)))
