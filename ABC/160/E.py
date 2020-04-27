import heapq
import sys
from itertools import accumulate
from collections import defaultdict

input = sys.stdin.readline

def main():
    X, Y, A, B, C = map(int, input().split())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    R = list(map(int, input().split()))
    ans = 0
    P_d = defaultdict(int)
    Q_d = defaultdict(int)
    R_d = defaultdict(int)

    for i in range(len(P)):
        P[i] = -P[i]
        P_d[P[i]] += 1
        
    for i in range(len(Q)):
        Q[i] = -Q[i]
        Q_d[Q[i]] += 1

    
    for i in range(len(R)):
        R[i] = -R[i]
        R_d[R[i]] += 1

    H = P + Q + R
    heapq.heapify(H)
    red = 0
    green = 0
    nocl = 0
    ans = 0
    for i in range(A + B + C):
        tmp = heapq.heappop(H)
        if red + green + nocl == X + Y:
            print(-ans)
            exit()

        if P_d[tmp] >= 1 and red < X:
            P_d[tmp] -= 1
            red += 1
            ans += tmp
        elif Q_d[tmp] >= 1 and green < Y:
            Q_d[tmp] -= 1
            green += 1
            ans += tmp
        elif R_d[tmp] >= 1:
            R_d[tmp] -= 1
            nocl += 1
            ans += tmp
    
if __name__ == "__main__":
    main()