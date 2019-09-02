def main():
    N = int(input())
    H = 0
    Cx = 0
    Cy = 0
    x = [0] * N
    y = [0] * N
    h = [0] * N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())

    for i in range(1, 101):
        for j in range(1,101):
            for k in range(N):
                if h[i] != 0:
                    H =

main()