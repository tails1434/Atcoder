from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    if A[0] >= 2:
        print(-1)
        exit()
    if A[0] == 1:
        if len(A) == 1:
            print(1)
            exit()
        else:
            print(-1)
            exit()
    ans = 1
    ans += A[N]
    C = [0] * (N+1)
    C[0] = 1
    C[N] += A[N]
    for i in range(N-1,0,-1):
        if A[i] == 0:
            ans += C[i+1]
            C[i] = C[i+1]
        else:
            ans += A[i] + C[i+1]
            C[i] = A[i] + C[i+1]
    print(C)
    for i in range(1,N+1):
        tmp = pow(2,C[i-1])
        if tmp <= C[i] - A[i]:
            C[i] = tmp - A[i]
    print(C)
    print(sum(C))






if __name__ == "__main__":
    main()