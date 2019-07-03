S = input()

min_A = 0
max_Z = 0

for i, s in enumerate(S):
    if s == 'A' and min_A == 0:
        min_A = i + 1
    elif s == 'Z':
        max_Z = i + 1

print(max_Z - min_A + 1)