N = int(input())

money = 0
c = int((N + (4 - 1)) / 4)
d = int((N + (7 - 1)) / 7)

for i in range(c+1):
    for j in range(d+1):
        if (i * 4) + (j * 7) == N:
            print('Yes')
            exit()
print('No')