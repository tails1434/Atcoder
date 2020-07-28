from collections import defaultdict

def main():
    N = int(input())
    d = defaultdict(lambda: defaultdict(int))
    R = [0] * N
    H = [0] * N
    for i in range(N):
        R[i], H[i] = map(int, input().split())
        d[R[i]][H[i]] += 1
    

    rate_win = defaultdict(int)
    pre = 0
    for i in sorted(d.keys()):
        rate_win[i] = pre
        pre += d[i][1] + d[i][2] + d[i][3]

    for i in range(N):
        win = rate_win[R[i]]
        lose = N - win - (d[R[i]][1] + d[R[i]][2] + d[R[i]][3])
        draw = 0
        if H[i] == 1:
            win += d[R[i]][2]
            lose += d[R[i]][3]
            draw += d[R[i]][1] - 1
        if H[i] == 2:
            win += d[R[i]][3]
            lose += d[R[i]][1]
            draw += d[R[i]][2] - 1
        if H[i] == 3:
            win += d[R[i]][1]
            lose += d[R[i]][2]
            draw += d[R[i]][3] - 1

        print(win, lose, draw)


if __name__ == "__main__":
    main()