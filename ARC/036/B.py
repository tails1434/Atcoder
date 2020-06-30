
def main():
    N = int(input())
    H = [int(input()) for _ in range(N)]
    L = [0] * N
    R = [0] * N
    for i in range(1,N):
        if H[i-1] < H[i]:
            L[i] = L[i-1] + 1

    for i in range(N-1,0,-1):
        if H[i-1] > H[i]:
            R[i-1] =R[i] + 1


    ans = 0
    for i in range(N):
        tmp = R[i] + L[i] + 1
        ans = max(ans,tmp)

    print(ans)


if __name__ == "__main__":
    main()