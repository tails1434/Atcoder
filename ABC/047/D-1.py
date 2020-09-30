def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    min_A = float('inf')
    cnt = 0
    profit = 0
    for i in range(N):
        min_A = min(min_A,A[i])
        diff_A = A[i] - min_A
        if profit == diff_A:
            cnt += 1
        elif profit < diff_A:
            cnt = 1
            profit = diff_A
    print(cnt)



if __name__ == "__main__":
    main()