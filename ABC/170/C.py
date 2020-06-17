def main():
    X, N = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    ans = 10000
    value = 100000
    for i in range(-1000,1000):
        if i in P:
            continue
        if ans > abs(X - i):
            ans = abs(X-i)
            value = i

    print(value)
            




if __name__ == "__main__":
    main()