N = int(input())
A = [int(input()) for _ in range(N)]

A = set(A)
A.remove(max(A))

print(max(A))