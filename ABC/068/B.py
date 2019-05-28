N = int(input())

res = -1
ans = -1
for i in range (1, N+1):
    count = 0
    a = i
    while a % 2 == 0:
        a /= 2
        count += 1
    
    if res < count:
        res = count
        ans = i

print(ans)