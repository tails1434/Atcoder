def main():
    A = int(input())
    ans = [0] * 10001
    for i in range(10,10001):
        tmp = 0
        cnt = 0
        s = str(i)
        for j in range(len(s)-1,-1,-1):
            tmp += int(s[j]) * (i ** cnt)
            cnt += 1
        ans[i] = tmp
    if A in ans:
        print(ans.index(A))
    else:
        print(-1)



if __name__ == "__main__":
    main()