def main():
    N = int(input())
    S = []
    for i in range(N):
        s, t = input().split()
        S.append([s,int(t)])
    X = input()
    ans = 0
    flag = False
    for i in range(N):
        if S[i][0] == X:
            flag = True
            continue
        if flag:
            ans += S[i][1]

    print(ans)



if __name__ == "__main__":
    main()