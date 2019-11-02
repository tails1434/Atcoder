def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))

    B = [0] * (N+1)

    for i in range(N,0,-1):
        tmp = 0
        for j in range(i,N+1,i):
            tmp ^= B[j]
        B[i] = tmp ^ A[i]

    cnt = 0
    ans = []
    for i in range(1,N+1):
        if B[i] == 1:
            cnt += 1
            ans.append(i)

    print(cnt)
    print(*ans)

main()