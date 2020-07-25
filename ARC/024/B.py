def main():
    N = int(input())
    colors = [int(input()) for _ in range(N)]
    if colors.count(1) == N or colors.count(0) == N:
        print(-1)
        exit()   
    colors += colors
    ans = 0
    cnt = 0
    for i in range(2*N-1):
        if colors[i] == colors[i+1]:
            cnt += 1
        else:
            ans = max(ans, cnt//2)
            cnt = 0
    ans = max(ans, cnt//2)
    print(ans + 1)
        

if __name__ == "__main__":
    main()