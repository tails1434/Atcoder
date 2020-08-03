from bisect import bisect_left

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    def check(x):
        index = bisect_left(A,x)
        ans = 0
        for i in range(index,N):
            tmp = -(-A[i] // x) - 1
            ans += tmp
        if ans <= K:
            return True
        else:
            return False
    ok = max(A)
    ng = 0
    while abs(ok- ng) > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()