def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if all([a > 0 for a in A]):
        pre = A[0]
        M = sum(A) - 2 * min(A)
        print(M)
        for i in range(1,N):
            if i != N - 1:
                print(pre, A[i])
                pre -= A[i]
            else:
                print(A[i], pre)
    elif all([a < 0 for a in A]):
        M = A[-1]
        for i in range(N-1):
            M -= A[i]
        print(M)
        pre = A[-1]
        for i in range(N-1):
            print(pre, A[i])
            pre -= A[i]
    else:
        cnt = 0
        M = 0
        for a in A:
            if a > 0:
                cnt += 1
            M += abs(a)
        print(M)
        if cnt == 1:
            pre = A[-1]
            for i in range(N-1):
                print(pre, A[i])
                pre -= A[i]
        else:
            pre = A[0]
            for i in range(1,N-1):
                if A[i] >= 0:
                    print(pre, A[i])
                    pre -= A[i]

            print(A[-1],pre)
            pre = A[-1] - pre
            for i in range(1,N-1):
                if A[i] < 0:
                    print(pre, A[i])
                    pre -= A[i]
                else:
                    break
                

if __name__ == "__main__":
    main()