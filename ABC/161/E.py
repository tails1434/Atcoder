def getWorkDay(S,N,C,K):
    cnt = 0
    day = 0
    flag = False
    L = [0] * N
    for i in range(N):
        if cnt >= K:
            break
        if flag:
            day += 1
            if S[i] == 'o' and day > C:
                cnt += 1
                L[i] = cnt
                day = 0
        else:
            if S[i] == 'o' and day == 0:
                cnt += 1
                L[i] = cnt
                day = 0
                flag = True
    return L

def main():
    N, K, C = map(int, input().split())
    S = list(input())
    L = getWorkDay(S,N,C,K)
    S.reverse()
    R = getWorkDay(S,N,C,K)
    R.reverse()
    cnt = 0
    max_R = max(R)
    for i in range(N-1,-1,-1):
        if R[i]:
            R[i] = max_R - cnt
            cnt += 1

    for i in range(N):
        if L[i] and R[i] and L[i] == R[i]:
            print(i+1)



if __name__ == "__main__":
    main()