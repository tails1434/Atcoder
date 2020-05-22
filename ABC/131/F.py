import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    V = 10 ** 5 + 5
    edge = [[] * (2 * V) for _ in range(2 * V)]
    visited = [False] * (2 * V)
    for i in range(N):
        x, y = map(int, input().split())
        y += V
        edge[x].append(y)
        edge[y].append(x)

    ans = 0
    for i in range(2 * V):
        if visited[i]:
            continue
        cnt = [0,0]
        q = deque([i])
        while q:
            s = q.pop() # dfsをやりたいのでpopleftではなくpop
            if visited[s]:
                continue
            visited[s] = True
            cnt[s//V] += 1
            for v in edge[s]:
                if visited[v]:
                    continue
                q.append(v)
        ans += cnt[0] * cnt[1]

    print(ans - N)


if __name__ == "__main__":
    main()