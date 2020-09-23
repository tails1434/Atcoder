from itertools import permutations

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    score = [[0] * 3 for _ in range(C)]
    for i in range(N):
        for j in range(N):
            for k in range(C):
                score[k][(i+j)%3] += D[c[i][j]-1][k]

    ans = float('inf')
    for balls in permutations(range(C),3):
        tmp = 0
        for i in range(3):
            tmp += score[balls[i]][i]
        ans = min(ans, tmp)
    print(ans)





if __name__ == "__main__":
    main()