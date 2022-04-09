import re

text = input()

pattern = r'(=|/)(?P<town>[A-Z][A-za-z]{2,})(\1)'
matches = re.finditer(pattern,text)

travel_points = 0
town = []
for match in matches:
    travel_points += len(match.group('town'))
    town.append(match.group('town'))

print(f"Destinations: {', '.join(town)}")
print(f'Travel Points: {travel_points}')