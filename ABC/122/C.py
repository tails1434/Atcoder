def main():
    N, Q = map(int, input().split())
    S = input()
    S_sum = [0] * (N+1)
    for i in range(N):
        S_sum[i+1] = S_sum[i] + (1 if S[i:i+2] == 'AC' else 0)

    for _ in range(Q):
        l, r = map(int, input().split())
        print(S_sum[r-1]-S_sum[l-1])


main()