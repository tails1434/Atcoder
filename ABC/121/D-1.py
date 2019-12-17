def func(x):
    x += 1
    res = 0
    for d in range(50):
        loop = 2 ** (d + 1)
        cnt = (x // loop) * (2 ** d)

        if (x % loop) - (2 ** d) > 0:
            cnt += (x % loop) - (2 ** d)

        if cnt % 2 != 0:
            res += 2 ** d
    return res


def main():
    A, B = map(int, input().split())

    print(func(B)^func(A-1))


if __name__ == "__main__":
    main()