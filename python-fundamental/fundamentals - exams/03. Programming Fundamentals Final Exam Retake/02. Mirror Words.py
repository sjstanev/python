import re

text = input()
pattern = r'(@|#)(?P<word_one>[A-Za-z]{3,})(\1){2}(?P<word_two>[A-Za-z]{3,})(\1)'
matches = re.finditer(pattern, text)

matched_words = []
valid_pairs_count = 0
is_mirror = False

# If you find valid pairs
for match in matches:
    # increase valid pairs counter
    valid_pairs_count += 1
    word_one = match.group('word_one')
    reversed_word = match.group('word_two')

    # If the second word, spelled backward, is the same as the first word and vice versa (casing matters!)
    if word_one == reversed_word[::-1]:
        is_mirror = True
        matched_words.append(f'{word_one} <=> {reversed_word}')

if not is_mirror and valid_pairs_count > 0:
    print(f"{valid_pairs_count} word pairs found!")
    print("No mirror words!")
elif not is_mirror and valid_pairs_count == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{valid_pairs_count} word pairs found!")
    print("The mirror words are:")
    print(*matched_words, sep= ', ')
