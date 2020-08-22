def main():
    N = int(input())
    B = list(map(int, input().split()))
    ans = []
    while B:
        for i in range(len(B)-1,-1,-1):
            if B[i] == i + 1:
                ans.append(B[i])
                B.pop(i)
                break
        else:
            print(-1)
            exit()
    for i in range(N-1,-1,-1):
        print(ans[i])





if __name__ == "__main__":
    main()