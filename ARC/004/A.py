import math

N = int(input())
P = [[int(i) for i in input().split()] for i in range(N)] 

max_dis = -1
for i in range(N):
    for j in range(N):
        dis = math.sqrt((P[i][0] - P[j][0]) ** 2 + (P[i][1] - P[j][1]) ** 2)
        if dis > max_dis:
            max_dis = dis

print(max_dis)