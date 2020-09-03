def main():
    N, x = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(1,N):
        tmp = A[i] + A[i-1]
        if tmp > x:
            tmp -= x
            cnt += tmp
            A[i] = max(0, A[i]-tmp)

    print(cnt)

if __name__ == "__main__":
    main()