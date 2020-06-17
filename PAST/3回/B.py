def main():
    N, M, Q = map(int, input().split())
    score = [N] * M
    solve = [[] for _ in range(N)]
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            n = q[1]
            ans = 0
            for i in solve[n-1]:
                ans += score[i]
            print(ans)
        else:
            n = q[1]
            m = q[2]
            score[m-1] -= 1
            solve[n-1].append(m-1)

    

if __name__ == "__main__":
    main()