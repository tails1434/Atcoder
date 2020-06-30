def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    C = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
        C[i] = A[i] + B[i]

    C.sort(reverse=True)
    ans = -sum(B)
    for i, c in enumerate(C):
        if i % 2 == 0:
            ans += C[i]
    
    print(ans) 

    
    



if __name__ == "__main__":
    main()