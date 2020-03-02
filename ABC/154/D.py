from itertools import accumulate

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    max_sum = 0
    index = -1
    sum_P = [0] + list(accumulate(P))
    for i in range(N + 1 - K):
        tmp = sum_P[i+K] - sum_P[i]
        if tmp > max_sum:
            max_sum = tmp
            index = i
        
    ans = 0
    for i in range(index,index + K):
        tmp = P[i] * (P[i] + 1) // 2
        ans += tmp / P[i]
    print(ans)



if __name__ == "__main__":
    main()