from itertools import permutations

def main():
    N, C = map(int, input().split())
    D = list(list(map(int, input().split())) for _ in range(C))
    c = list(list(map(int, input().split())) for _ in range(N))
    cost = [[0] * (C + 5) for _ in range(3)]

    for k in range(C):
        for i in range(N):
            for j in range(N):
                cost[(i + j) % 3][k + 1] += D[c[i][j]-1][k]

    ans = float('inf')

    for a, b, c in permutations(range(1,C+1), 3):
        tmp = cost[0][a] + cost[1][b] + cost[2][c]
        ans = min(tmp, ans)

    print(ans)


    







if __name__ == "__main__":
    main()