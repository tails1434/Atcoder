N = int(input())
T,A = map(int, input().split())
H = list(map(int, input().split()))

ans = float('inf')
index = -1
value = float('inf')

for i in range(N):
    ave_T = 0
    ave_T = T - H[i] * 0.006
    if (abs(A - ave_T)) < ans:
        ans = abs(A - ave_T)
        index = i + 1
        value = A[i]

print(index)