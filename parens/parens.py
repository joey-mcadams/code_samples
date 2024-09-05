parens = "()()()()("
# parens = ")))((("

first_pos = 0
last_pos = 0
first_found = False
last_found = False

for i, char in enumerate(parens):
    if char == '(':
        first_found = True
        first_pos = i
        break

for i in range(len(parens) - 1, 0, -1):
    if parens[i] == ')':
        last_found = True
        last_pos = i
        break

if first_found and last_found and (first_pos < last_pos):
    print(last_pos - first_pos)
else:
    print("Error")





