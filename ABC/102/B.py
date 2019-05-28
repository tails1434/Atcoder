N = int(input())
A = list(map(int, input().split()))

min_A = float('inf')
max_A = -1

for i in range(N):
    if A[i] < min_A:
        min_A = A[i]
    if A[i] > max_A:
        max_A = A[i]


print(max_A - min_A)