def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    B = []
    minus = [False] * N
    flag = False
    for i in range(N):
        if A[i] == 0:
            continue
        if A[i] < 0:
            minus[i] = True
        if A[i] > 0:
            flag = True
        B.append([abs(A[i]),i])

    if not flag:
        if N - len(B) != 0:
            print(0)
            exit()
        B.sort()
        ans = 1
        for i in range(K):
            ans *= A[B[i][1]]
            ans %= MOD
            
        print(ans)
        exit()

    if K >= len(B):
        if len(B) == N:
            ans = 1
            for i in range(N):
                ans *= A[i]
                ans %= MOD
            print(ans)
            exit()
        else:
            print(0)
            exit()

    B.sort(reverse=True)
    cnt = 0
    cand = []
    min_minus = -1
    min_plus = -1
    for i in range(K):
        if minus[B[i][1]]:
            cnt += 1
            min_minus = B[i][1]
        else:
            min_plus = B[i][1]
        cand.append(B[i][1])
    ans = 1

    if cnt % 2 == 0:
        for i in cand:
            ans *= A[i]
            ans %= MOD
    else:
        if cnt == minus.count(True):
            cand.pop(min_minus)
            for i in range(K,len(B)):
                if B[i][0] > 0:
                    cand.append(B[i][1])
                    break
            else:
                cand.append(min_minus)
            for i in cand:
                ans *= A[i]
                ans %= MOD
        else:
            if A[min_plus] > A[min_minus]:
                cand.pop(min_minus)
                for i in range(K,len(B)):
                    if B[i][0] > 0:
                        cand.append(B[i][1])
                        break
                else:
                    cand.append(min_minus)
            elif A[min_plus] < A[min_minus]:
                cand.pop(min_plus)
                for i in range(K,len(B)):
                    if B[i][0] < 0:
                        cand.append(B[i][1])
                        break
            else:
                cand.pop(max(min_plus,min_minus))
                cand.append(max(min_plus,min_minus) + 1)

            for i in cand:
                ans *= A[i]
                ans %= MOD

            
    print(ans)

    


if __name__ == "__main__":
    main()