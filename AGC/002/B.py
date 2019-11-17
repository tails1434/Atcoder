def main():
    N, M = map(int, input().split())
    cnt = [1] * N
    red = [False] * N
    red[0] = True
    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        cnt[x] -= 1
        cnt[y] += 1
        if red[x] == True:
            red[y] = True
            if cnt[x] == 0:
                red[x] = False
    ans = 0
    for i in red:
        if i:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()