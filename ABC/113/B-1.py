def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    ans = float('inf')
    cnt = 0
    for i, h in enumerate(H):
        tmp = abs(A - (T - h * 0.006))
        if ans > tmp:
            ans = tmp
            cnt = i + 1

    print(cnt)


main()