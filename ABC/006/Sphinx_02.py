import sys

N,M = map(int, input().split())

# x + y + z = N
# 2x + 3y + 4z = M
#z = (M-x*2)-3*(N-x)
#y = N-x-z

for i in range (0, N+1):
    z = (M-i*2)-3*(N-i)
    y = N-i-z
    if y >= 0 and z >= 0:
        print(i,y,z)
        sys.exit()

print("-1 -1 -1")