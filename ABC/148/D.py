def main():
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 1
    ans = 0
    for i in range(N):
        if cnt == A[i]:
            cnt += 1
            ans += 1
    
    if ans == 0:
        print(-1)
    else:
        print(N-ans)




if __name__ == "__main__":
    main()