from itertools import accumulate
from bisect import bisect_left


N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = [0] + list(accumulate(A))

def check(X):
    cnt = 0
    for i in range(N):
        cnt += N - bisect_left(A, X - A[i])
    return cnt >= M


def main():

    ng = 10 ** 9
    ok = 0
    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid

    ans = 0
    cnt = 0
    for i in range(N):
        tmp = bisect_left(A, ok - A[i])
        cnt += N - tmp
        ans += B[N] - B[tmp]
        ans += A[i] * (N - tmp)
    ans -= ok * (cnt - M)
    print(ans)




if __name__ == "__main__":
    main()