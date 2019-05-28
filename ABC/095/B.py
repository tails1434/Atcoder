N, X = map(int, input().split())
m = [int(input()) for i in range(N)]

diff = X - sum(m)
items = diff // min(m)
print( items + N)