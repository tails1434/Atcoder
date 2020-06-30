def main():
    N, M = map(int, input().split())
    for i in range(N+1):
        k = i - 3 * N + M
        j = 4*N -M - 2*i
        tmp = 2 * i + 3 * j + 4 * k
        if tmp == M and (i+j+k) == N and i >= 0 and j >= 0 and k >= 0:
            print(i,j,k)
            exit()

    print(-1,-1,-1)
if __name__ == "__main__":
    main()