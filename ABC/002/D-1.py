def main():
    N, M = map(int, input().split())
    edge = [[False] * N for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        edge[x][y] = True
        edge[y][x] = True
    ans = 0
    for i in range(2**N):
        cand = []
        for j in range(N):
            if (i >> j) & 1:
                cand.append(j)
        
        flag = True
        for n in cand:
            for m in cand:
                if n == m:
                    continue
                if not edge[n][m]:
                    flag = False
                    break
            if not flag:
                break

        if flag:
            ans = max(ans, len(cand))

    print(ans)


if __name__ == "__main__":
    main()