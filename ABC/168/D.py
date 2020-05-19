from collections import deque

def main():
    N, M = map(int, input().split())
    edge = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        edge[A].append(B)
        edge[B].append(A)
    cnt = [float('inf')] * N  
    cnt[0] = 0
    Q = deque([0])
    visited = [False] * N
    visited[0] = True
    while Q:
        s = Q.popleft()

        for v in edge[s]:
            if visited[v]:
                continue
            cnt[v] = s + 1
            visited[v] = True
            Q.append(v)

    for i in range(N):
        if cnt[i] == float('inf'):
            print('No')
            exit()
    print('Yes')
    for i in range(1,N):
        print(cnt[i])


if __name__ == "__main__":
    main()