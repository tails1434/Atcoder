n = int(input())
A = list(map(int, input().split()))

cnt = 0
for a in A:
    while a % 2 == 0 or (a - 2) % 3 == 0:
        a -= 1
        cnt += 1
        

print(cnt)