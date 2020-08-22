def main():
    N = int(input())
    robot = []
    for _ in range(N):
        X, L = map(int, input().split())
        robot.append([X-L,X+L])

    robot.sort(key=lambda x: x[1])
    cnt = 1
    l = robot[0][1]
    for i in range(1,N):
        if l <= robot[i][0]:
            cnt += 1
            l = robot[i][1]

    print(cnt)


if __name__ == "__main__":
    main()