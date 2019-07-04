X = int(input())

ans = 0
for i in range(1,X+1):
    ans += i
    if ans >= X:
        print(i)
        exit()