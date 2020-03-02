
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    div = sorted(divisor(sum(A)), reverse=True)
    ans = 0
    for d in div:
        mod = [0] * N
        for i in range(N):
            mod[i] = A[i] % d
        sort_mod = sorted(mod)
        cnt = float('inf')
        rsum = d * N - sum(sort_mod)
        lsum = 0
        for j in range(N):
            lsum += sort_mod[j]
            rsum -= d - sort_mod[j]
            tmp = max(lsum, rsum)
            cnt = min(cnt, tmp)
        if cnt <= K:
            print(d)
            exit()

    


if __name__ == "__main__":
    main()