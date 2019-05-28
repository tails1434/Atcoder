s = input()

index_A = float('inf')
index_Z = -1

for i in range(len(s)):
    if s[i] == 'A':
        if i < index_A:
            index_A = i
    elif s[i] == 'Z':
        if i > index_Z:
            index_Z = i

print(index_Z - index_A + 1)