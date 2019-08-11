N = int(input())
A = list(map(int, input().split()))

ans = float('inf')
for i in range(N):
    cnt = 0

    while A[i] % 2 == 0:
        A[i] /= 2
        cnt += 1    
    if ans > cnt:
        ans = cnt

print(ans)