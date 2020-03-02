from bisect import bisect_right

def main():
    N = int(input())
    L = list(map(int, input().split()))
    sort_L = sorted(L)
    ans = 0
    for i in range(N-2):
        for j in range(i,N-1):
            if i == j:
                continue
            ok = j
            ng = N
            tmp = sort_L[i] + sort_L[j]
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if sort_L[mid] < tmp:
                    ok = mid
                else:
                    ng = mid

            ans += ok - j

    print(ans)



if __name__ == "__main__":
    main()