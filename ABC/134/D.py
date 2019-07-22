def main():
    N = int(input())
    a = [0] + list(map(int, input().split()))

    b = [0] * (N + 1) 

    for i in range(N,0,-1):
        sum = 0
        for j in range(2*i, N+1, i):
            sum += b[j]
        if sum % 2 != a[i] % 2:
            b[i] = 1
    
    ans = []
    for i in range(1,N+1):
        if b[i] == 1:
            ans.append(i)
    
    print(len(ans))
    print(*ans)

main()