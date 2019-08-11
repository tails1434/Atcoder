def main():
    N, A, B = map(int, input().split())

    ans = 0
    for i in range(1,N+1):
        tmp = 0
        for j in str(i):
            tmp += int(j)
        if A <= tmp <= B:
            ans += i

    print(ans) 

main()