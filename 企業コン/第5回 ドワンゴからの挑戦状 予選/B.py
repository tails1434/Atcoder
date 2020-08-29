from itertools import accumulate

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    B = [0] + list(accumulate(A))
    cand = []
    for i in range(N+1):
        for j in range(i+1,N+1):
            cand.append(B[j] - B[i])
    ans = 0
    for i in range(40):
        bit = 1 << (39 - i)
        cnt = 0
        new_cand = []
        for c in cand:
            if c & bit:
                cnt += 1
                new_cand.append(c)

        if cnt >= K:
            ans += 2 ** (39 - i)
            cand = new_cand


    print(ans)




if __name__ == "__main__":
    main()