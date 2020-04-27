from collections import defaultdict

def main():
    N, P = map(int, input().split())
    S = list(map(int,list(input())))
    S_mod = [0] * N
    if P == 2:
        for i in range(N-1,-1,-1):
            if S[i] % 2 == 0:
                S_mod[i] = 1
        S_mod.reverse()
        ans = 0
        cnt = 0
        for i in range(N):
            if S_mod[i] == 1:
                cnt += 1
                ans += cnt
            else:
                ans += cnt
        print(ans)
        exit()
    if P == 5:
        for i in range(N-1,-1,-1):
            if S[i] % 5 == 0:
                S_mod[i] = 1
        S_mod.reverse()
        ans = 0
        cnt = 0
        for i in range(N):
            if S_mod[i] == 1:
                cnt += 1
                ans += cnt
            else:
                ans += cnt
        print(ans)
        exit()



    ten = 1
    for i in range(N-1,-1,-1):
        S_mod[i] = (S[i] * ten) % P
        ten *= 10
        ten %= P
    S_mod.reverse()
    S_acc = [0] * (N+1)
    for i in range(N):
        S_acc[i+1] = (S_acc[i] + S_mod[i]) % P
    d = defaultdict(int)
    for i in range(N+1):
        d[S_acc[i]] += 1
    ans = 0
    for i, j in d.items():
        if j >= 2:
            ans += (j * (j-1)) // 2

    print(ans)
    





if __name__ == "__main__":
    main()