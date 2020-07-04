def runlength(S):
    A = []
    tmp = S[0]
    cnt = 0
    for i in range(len(S)):
        if S[i] == tmp:
            cnt += 1
        else:
            A.append(cnt)
            tmp = S[i]
            cnt = 1
    else:
        A.append(cnt)
    return A

def main():
    X = input()
    Y = runlength(X)
    if X[0] == 'T':
        Y = [0] + Y
    
    if X[-1] == 'S':
        Y += [0]

    ans = len(X)
    amari = 0
    for i in range(0,len(Y),2):
        ans -= 2 * min(amari + Y[i], Y[i+1])
        amari = max(0, amari + Y[i] - Y[i+1])

    print(ans)


if __name__ == "__main__":
    main()