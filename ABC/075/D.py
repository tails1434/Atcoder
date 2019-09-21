def main():
    N, K = map(int, input().split())
    x = [0] * N
    y = [0] * N

    for i in range(N):
        x[i], y[i] = map(int, input().split())

    ans = float('inf')
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if x[i] < x[j] and y[k] < y[l]:
                        cnt = 0
                        lx = x[i]
                        rx = x[j]
                        by = y[k]
                        uy = y[l]

                        for n in range(N):
                            if lx <= x[n] and x[n] <= rx and by <= y[n] and y[n] <= uy:
                                cnt += 1

                        if cnt >= K:
                            ans = min(ans, (rx - lx) * (uy - by))

    print(ans)

main()