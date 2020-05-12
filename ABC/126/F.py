def main():
    M, K = map(int, input().split())
    if K >= 2 ** M:
        print(-1)
        exit()
    
    if K == 1 and M == 1:
        print(-1)
        exit()
    
    
    if K == 0 and M == 1:
        print(0,0,1,1)
        exit()

    ans = []
    for i in range(2**M):
        if i == K:
            continue
        ans.append(i)
    ans.append(K)

    for i in range(2**M-1,-1,-1):
        if i == K:
            continue
        ans.append(i)
    ans.append(K)

    print(*ans)

    


if __name__ == "__main__":
    main()