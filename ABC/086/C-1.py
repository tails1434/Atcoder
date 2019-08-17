def main():
    N = int(input())

    t = [0] * (N + 1)
    x = [0] * (N + 1)
    y = [0] * (N + 1)

    for i in range(1, N+1):
        t[i], x[i], y[i] = map(int, input().split())
        diff_t = t[i] - t[i-1]
        dist = abs(x[i] - x[i-1]) + abs(y[i] - y[i-1])
        if diff_t < dist:
            print('No')
            exit()
        elif diff_t >= dist:
            if diff_t % 2 == dist % 2:
                continue
            else:
                print('No')
                exit()
    print('Yes')


main()