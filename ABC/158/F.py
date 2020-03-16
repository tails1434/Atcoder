def main():
    N = int(input())
    robot = []
    for _ in range(N):
        X, D = map(int, input().split())
        robot.append((X,D))

    robot.sort(reverse=True)
    MOD = 998244353

    cnt = [0] * N
    cnt[N-1] = 1
    for i in range(1,N):
        if robot[i][0] + robot[i][1] > robot[i-1][0]:
            cnt[N-1-i] += 1 + cnt[N-i]
        else:
            cnt[N-1-i] = 1

    print(cnt)

if __name__ == "__main__":
    main()