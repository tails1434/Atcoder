def isOK(mid,N,K,sort_F,sort_A):
    cnt = 0
    for i in range(N):
        cnt += max(sort_A[i] - (mid // sort_F[i]),0)
    return cnt <= K

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    F = list(map(int, input().split()))
    sort_A = sorted(A)
    sort_F = sorted(F, reverse=True)

    ng = -1
    ok = 10 ** 12 + 5
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid,N,K,sort_F,sort_A):
            ok = mid
        else:
            ng = mid

    print(ok)



if __name__ == "__main__":
    main()