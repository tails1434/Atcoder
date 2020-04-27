def main():
    N, M = map(int, input().split())
    ball = [1] * N
    red = [False] * N
    red[0] = True
    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        ball[x] -= 1
        ball[y] += 1
        if red[x]:
            red[y] = True
        if ball[x] == 0:
            red[x] = False

    ans = 0
    for i in range(N):
        if red[i]:
            ans += 1

    print(ans)




if __name__ == "__main__":
    main()