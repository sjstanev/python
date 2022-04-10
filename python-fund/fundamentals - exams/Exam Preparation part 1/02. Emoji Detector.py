import re

text = input()
cool_threshold_sum = 1
count_of_emojis = 0

pattern_digit = r'(\d)'
cool_threshold = re.findall(pattern_digit, text)
for x in cool_threshold:
    cool_threshold_sum *= int(x)

pattern = r'(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})(\1)'
matches = re.finditer(pattern, text)

all_emojis = []
for match in matches:
    count_of_emojis += 1
    emoji = match.group('emoji')
    threshold = 0
    # for every emoji find his thresholdsum\
    # the coolness of the emoji is determined by summing all the ASCII values of all letters in the emoji.
    for char in emoji:
        threshold += ord(char)
        # find max coolThresholdSum
    if threshold > cool_threshold_sum:
        all_emojis.append(match.group(0))

print(f"Cool threshold: {cool_threshold_sum}")
print(f"{count_of_emojis} emojis found in the text. The cool ones are:")
for emoji in all_emojis:
    print(emoji)