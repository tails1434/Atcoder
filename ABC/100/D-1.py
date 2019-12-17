def main():
    N, M = map(int, input().split())
    x = [0] * N
    y = [0] * N
    z = [0] * N
    for i in range(N):
        x[i], y[i], z[i] = map(int, input().split())

    ans = 0
    for i in [-1,1]:
        for j in [-1,1]:
            for k in [-1,1]:
                cand_list = []
                for n in range(N):
                    tmp = i * x[n] + j * y[n] + k * z[n]
                    cand_list.append(tmp)
                cand_list.sort(reverse=True)
                a = 0
                for m in range(M):
                    a += cand_list[m]
                ans = max(ans, a)

    print(ans)


    


if __name__ == "__main__":
    main()