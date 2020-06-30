def main():
    N = int(input())
    ans = []
    for i in range(N-154,N):
        if i <= 0:
            continue
        tmp = i
        for j in str(i):
            tmp += int(j)
        if tmp == N:
            ans.append(i)

    print(len(ans))
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()