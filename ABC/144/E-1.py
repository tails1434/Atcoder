N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
sort_A = sorted(A)
sort_F = sorted(F,reverse=True)

def check(x):
    cnt = 0
    for i in range(N):
        tmp = x // sort_F[i]
        cnt += max(0, sort_A[i] - tmp)
    return cnt <= K



def main():
    ok = 10 ** 13
    ng = -1

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid

    print(ok) 

if __name__ == "__main__":
    main()