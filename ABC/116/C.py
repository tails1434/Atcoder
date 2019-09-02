def main():
    N = int(input())
    h = list(map(int, input().split()))

    ans = 0
    while True:
        # max(h)が0になったら終了
        if max(h) == 0:
            break

        i = 0
        while i < N:
            # h[i]が0なら次に進む
            if h[i] == 0:
                i += 1
            else:
                # h[i]が0になるところまでとりあえず-1する
                ans += 1
                while (i < N and h[i] > 0):
                    h[i] -= 1
                    i += 1

    print(ans)


main()