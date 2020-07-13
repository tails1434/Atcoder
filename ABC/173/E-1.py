def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    plus = []
    minus = []
    for a in A:
        if a >= 0:
            plus.append(a)
        else:
            minus.append(a)
    # 答えが負になる場合をFalse
    flag = False
    if len(plus) > 0:
        if N == K:
            flag = (len(minus) % 2) == 0
        if N > K:
            flag = True
    elif len(plus) == 0:
        flag = (K % 2) == 0
    
    MOD = 10 ** 9 + 7
    ans = 1
    if flag:
        plus.sort(reverse=True)
        minus.sort()
        if K % 2 == 1:
            ans = plus.pop(0)
        B = []
        for i in range(0,len(plus),2):
            if i + 1 < len(plus):
                B.append(plus[i]*plus[i+1])
        for i in range(0,len(minus),2):
            if i + 1 < len(minus):
                B.append(minus[i]*minus[i+1])
        B.sort(reverse=True)
        for j in range(K//2):
            ans *= B[j]
            ans %= MOD
    else:
        A.sort(reverse=True)
        for i in range(K):
            ans *= A[i]
            ans %= MOD

    print(ans)
        


if __name__ == "__main__":
    main()