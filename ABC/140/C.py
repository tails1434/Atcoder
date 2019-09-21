def main():
    N = int(input())
    B = [0] + list(map(int, input().split()))
    
    A = [float('inf')] * N
    for i in range(N-1,0,-1):
        A[i] = min(A[i],B[i])
        A[i-1] = min(A[i-1],B[i])

    print(sum(A))

main()