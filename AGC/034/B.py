def main():
    S = list(input())
    N = len(S)
    if N <= 2:
        print(0)
        exit()
    T = []
    flag = False
    for i in range(N-1):
        if flag:
            flag = False
            continue

        if S[i] == 'B' and S[i+1] == 'C':
            T.append('D')
            flag = True
        else:
            T.append(S[i])
        
    if not (S[i-2] == 'B' and S[i-1] == 'C'):
        T.append(S[i-1])
    
    M = len(T)
    d = [0] * T.count('D')
    ans = 0
    a = 0
    for i in range(M):
        if T[i] == 'A':
            a += 1
        elif T[i] == 'D':
            ans += a
        else:
            a = 0
    print(ans)

if __name__ == "__main__":
    main()