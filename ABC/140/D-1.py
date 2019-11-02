def runlength(S):
    d = []
    cnt = 1
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            d.append(cnt)
            cnt = 1
        else:
            cnt += 1
    else:
        d.append(cnt)
    return d

def main():
    N, K = map(int, input().split())
    S = input()
    D = runlength(S)
    cnt = 0
    for d in D:
        cnt += d-1
    ans = min(N-1,cnt+2*K)
    print(ans)

if __name__ == "__main__":
    main()