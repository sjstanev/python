import re

pattern = r'(#|\|)(?P<food>[A-Za-z\s]+)(\1)(?P<day>\d{2}/\d{2}/\d{2})(\1)(?P<calories>[1-9][0-9]{1,3}|10000)(\1)'
text = input()
calories = 0
result = []
matches = re.finditer(pattern,text)

for match in matches:
    calories += int(match.group('calories'))
    result.append(f"Item: {match.group('food')}, Best before: {match.group('day')}, Nutrition: {match.group('calories')}")

print(f'You have food to last you for: {calories//2000} days!')

for i in result:
    print(i)