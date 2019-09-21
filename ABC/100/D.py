def main():
    N, M = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in [-1,1]:
        for j in [-1,1]:
            for k in [-1,1]:
                tmp = []
                for x, y, z in X:
                    tmp.append(i*x + j*y + k*z)
                tmp.sort(reverse=True)
                ans = max(ans, sum(tmp[:M]))
    
    print(ans)

main()