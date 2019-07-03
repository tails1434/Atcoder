N = int(input())
S = input()

max_x = 0
x = 0
for s in S:
    if s == 'I':
        x += 1
    else:
        x -= 1
    
    if max_x < x:
        max_x = x

print(max_x)
