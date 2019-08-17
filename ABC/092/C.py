def main():
    N = int(input())
    A = [0] + list(map(int, input().split())) + [0]

    dist = 0
    for i in range(1, N+2):
        dist += abs(A[i] - A[i-1])
    
    for i in range(1, N+1):
        ans = dist - abs(A[i] - A[i-1]) - abs(A[i+1] - A[i]) + abs(A[i+1] - A[i-1])
        print(ans)

main()