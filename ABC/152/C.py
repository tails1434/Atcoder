def main():
    N = int(input())
    P = list(map(int, input().split()))
    min_P = float('inf')
    cnt = 0
    for i in range(N):
        if P[i] <= min_P:
            cnt += 1
        min_P = min(min_P, P[i])

    print(cnt)


if __name__ == "__main__":
    main()