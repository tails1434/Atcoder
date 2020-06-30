def main():
    N, M = map(int, input().split())
    cnt = [-1] * N
    for i in range(M):
        a = int(input())
        a -= 1
        cnt[a] = i
    tmp = []
    ans = []
    for i in range(N):
        if cnt[i] == -1:
            ans.append(i+1)
        else:
            tmp.append([cnt[i], i+1])
    tmp.sort(reverse=True)
    ans2 = []
    for i, j in tmp:
        ans2.append(j)
    ans3 = ans2 + ans
    for a in ans3:
        print(a)


if __name__ == "__main__":
    main()