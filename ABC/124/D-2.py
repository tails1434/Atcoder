from itertools import accumulate

def runlength(S):
    cnt = 1
    A = []
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            A.append(cnt)
            cnt = 1
    else:
        A.append(cnt)

    return A


def main():
    N, K = map(int, input().split())
    S = input()
    T = []
    prev = '1'
    cnt = 0
    for c in S:
        if prev == c:
            cnt += 1
        else:
            T.append(cnt)
            cnt = 1
        prev = c
    
    T.append(cnt)    
    if prev == '0':
        T.append(0)

    w = 2 * K + 1
    if len(T) <= w:
        print(N)
        exit()

    acc = [0] + list(accumulate(T))
    ans = 0
    for i in range(0, len(T) - w + 1, 2):
        ans = max(ans, acc[i+w] -acc[i])

    print(ans)

if __name__ == "__main__":
    main()