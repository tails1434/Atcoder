N = int(input())
d = [int(input()) for i in range(N)]

d_unique = list(set(d))

print(len(d_unique))