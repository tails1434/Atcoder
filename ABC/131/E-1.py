def main():
    N, K = map(int, input().split())
    max_K = (N - 1) * (N - 2) // 2
    if K > max_K:
        print(-1)
        exit()

    ans = []
    for i in range(2, N+1):
        ans.append((1,i))

    cand = []
    for i in range(2,N):
        for j in range(i+1,N+1):
            cand.append((i,j))

    
    for i in range(max_K - K):
        a, b = cand.pop()
        ans.append((a,b))

    print(len(ans))
    for u, v in ans:
        print(u,v)



if __name__ == "__main__":
    main()