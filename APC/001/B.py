def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if sum(A) > sum(B):
        print('No')
        exit()
    
    cnt = 0
    for i in range(N):
        if B[i] > A[i]:
            cnt += (B[i] - A[i]) // 2
        else:
            cnt -= (A[i] - B[i])

    if cnt >= 0:
        print('Yes')
    else:
        print('No')
    


if __name__ == "__main__":
    main()