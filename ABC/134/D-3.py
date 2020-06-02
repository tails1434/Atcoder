def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] * (N + 1)
    ans = []
    for i in range(N,0,-1):
        B[i] = A[i]
        j = 2
        while i * j < (N + 1):
            B[i] ^= B[i * j]
            j += 1
        
        if B[i] % 2 == 1:
            ans.append(i)

    print(len(ans))
    print(*ans)
        





if __name__ == "__main__":
    main()