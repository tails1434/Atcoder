from collections import deque
from itertools import accumulate
import sys
sys.setrecursionlimit(1000000)

def func(x):
    return x - 1

def main():
    N, K = map(int, input().split())
    P = list(map(func,map(int, input().split())))
    C = list(map(int, input().split()))
    flag = False
    for i in range(N):
        if C[i] >= 0:
            flag = True
    if not flag:
        print(max(C))
        exit()
    cand = []
    visited = [False] * N
    for i in range(N):
        if not visited[i]:
            Q = deque([i])
            tmp = []
            while Q:
                x = Q.pop()
                visited[x] = True
                v = P[x]
                if not visited[v]:
                    Q.append(v)
                    tmp.append(C[v])
            tmp.append(C[v])
            cand.append(tmp+tmp)
    ans = 0
    for item in cand:
        tmp_score = 0
        L = len(item) // 2
        S = sum(item) // 2
        D = [0] + list(accumulate(item))
        if K <= L:
            cnt = K
            for l in range(L):
                for j in range(cnt):
                    tmp = D[l+j+1] - D[l] 
                    tmp_score = max(tmp_score, tmp)
            ans = max(ans, tmp_score)
        else:
            if S > 0:
                cnt = K % L
                for l in range(L):
                    for j in range(cnt):
                        tmp = D[l+j+1] - D[l]
                        tmp_score = max(tmp_score, tmp)
                tmp_score += (K // L) * S
                ans = max(ans, tmp_score)
            else:
                cnt = min(K,L+1)
                for l in range(L):
                    for j in range(cnt):
                        tmp = D[l+j+1] - D[l] 
                        tmp_score = max(tmp_score, tmp)
                ans = max(ans, tmp_score)

    print(ans)
            




if __name__ == "__main__":
    main()