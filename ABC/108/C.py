def main():
    N, K = map(int, input().split())

    x = 0
    y = 0
    for i in range(1, N + 1):
        if i % K == 0:
            x += 1
        elif i % K == int(K / 2):
            y += 1

    if K % 2 == 0:
        print(x ** 3 + y ** 3)
    else:
        print(x ** 3)


main()