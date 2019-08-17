def main():
    N, X = map(int, input().split())
    min_m = float('inf')
    cnt = 0
    for i in range(N):
        m = int(input())
        X -= m
        cnt += 1
        if min_m > m:
            min_m = m

    cnt += X // min_m
    print(cnt)

main()