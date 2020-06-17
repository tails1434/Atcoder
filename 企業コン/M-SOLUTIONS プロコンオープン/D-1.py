from collections import deque

def main():
    N = int(input())
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
    C = list(map(int, input().split()))
    C.sort(reverse=True)
    ans = [0] * N
    Q = deque([0])
    cnt = 0
    ans[0] = C[0]
    while Q:
        s = Q.pop()
        for v in edge[s]:
            if ans[v]:
                continue
            cnt += 1
            ans[v] = C[cnt]
            Q.append(v)

    print(sum(C) - max(C))
    print(*ans)


if __name__ == "__main__":
    main()