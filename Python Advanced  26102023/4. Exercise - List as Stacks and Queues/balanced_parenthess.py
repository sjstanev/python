expression = input()

opennig_brackets = []

pairs = {
    '(': ')',
    '{': '}',
    '[': ']',
}
balanced = True

for ch in expression:
    if ch in '({[':
        opennig_brackets.append(ch)
    elif not opennig_brackets:
        balanced = False
    else:
        last_opening_bracket = opennig_brackets.pop()
        if pairs[last_opening_bracket] != ch:
            balanced = False

    if not balanced:
        break

if not balanced or opennig_brackets:
    print("NO")
else:
    print("YES")
