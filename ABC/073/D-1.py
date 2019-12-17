from itertools import permutations

def main():
    N, M, R = map(int, input().split())
    r = list(map(int, input().split()))
    d = [[float('inf')] * N for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        d[A][B] = C
        d[B][A] = C
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    ans = float('inf')
    for D in list(permutations(r)):
        tmp = 0
        for i in range(len(D)-1):
            tmp += d[D[i]-1][D[i+1]-1]
        ans = min(ans, tmp)

    print(ans)



           



if __name__ == "__main__":
    main()