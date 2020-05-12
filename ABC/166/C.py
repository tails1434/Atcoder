def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    edge =  [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        edge[A].append(H[B])
        edge[B].append(H[A])
    ans = 0
    for i in range(N):
        if not edge[i]:
            ans += 1
        elif H[i] > max(edge[i]):
            ans += 1

    print(ans)
        


    

        


if __name__ == "__main__":
    main()