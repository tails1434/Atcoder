def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = -(10 ** 5)
    for i in range(N):
        aoki = []
        for j in range(N):
            if i == j: continue

            left, right = min(i,j), max(i,j)
            T = A[left: right+1]
            aoki.append(sum(T[1::2]))

        j = aoki.index(max(aoki))
        left, right = min(i, j), max(i, j)
        T = A[left: right+1]
        ans = max(ans, sum(T[0::2]))
                        
    print(ans)
                        

if __name__ == "__main__":
    main()