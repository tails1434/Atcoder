def main():
    N, C = map(int, input().split())
    D = [[0] * (10 ** 5 + 5) for _ in range(C)]    
    for _ in range(N):
        s, t, c = map(int, input().split())
        c -= 1
        D[c][s] += 1
        D[c][t] -= 1
    
    for c in range(C):
        for i in range(1,10 ** 5 + 1):
            D[c][i] += D[c][i-1]

    for c in range(C):
        for i in range(1,10 ** 5 + 1):
            if D[c][i] == 1:
                D[c][i-1] = 1

    S = [0] * (10 ** 5 + 5)
    for c in range(C):
        for i in range(10 ** 5 + 1):
            S[i] += D[c][i]

    print(max(S))

if __name__ == "__main__":
    main()