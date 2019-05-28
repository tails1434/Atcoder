from collections import deque

R,C = map(int, input().split())
sy,sx = map(int, input().split())
gy,gx = map(int, input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1

c=[[x for x in input()] for i in range(R)]

visited = [[-1] * C for j in range(R)]

print(visited)