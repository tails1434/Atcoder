import sys
sys.setrecursionlimit(1000000)

def func(x):
    return x - 1
def main():
    N, K = map(int, input().split())
    P = list(map(func,map(int, input().split())))
    C = list(map(int, input().split()))
    ans = -float('inf')
    for si in range(N):
        x = si
        tot = 0
        S = []
        while True:
            x = P[x]
            S.append(C[x])
            tot += C[x]
            if x == si:
                break
        l = len(S)
        t = 0
        for i in range(l):
            t += S[i]
            if i + 1 > K:
                break
            now = t
            if tot > 0:
                e = (K-(i+1)) // l
                now += tot*e
            ans = max(ans, now)

    print(ans)


if __name__ == "__main__":
    main()