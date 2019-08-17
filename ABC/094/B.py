def main():
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))

    lower_cnt = 0
    upper_cnt = 0

    for a in A:
        if a < X:
            lower_cnt += 1
        elif a > X:
            upper_cnt += 1

    print(min(upper_cnt, lower_cnt))

main()