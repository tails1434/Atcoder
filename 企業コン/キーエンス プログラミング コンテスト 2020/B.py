def main():
    N = int(input())
    A = []
    for _ in range(N):
        X, L = map(int, input().split())
        A.append((X, L))
 
    A.sort()
    cnt = 0
    right = 0
    left = 0
    for i in range(N):
        if i == 0:
            left = A[i][0] - A[i][1]
            right = A[i][0] + A[i][1]
        else:
            tmp_left = A[i][0] - A[i][1]
            tmp_right = A[i][0] + A[i][1]
            if tmp_right < right:
                left = tmp_left
                right = tmp_right
                cnt += 1
            elif tmp_left < right:
                cnt += 1
            else:
                left = A[i][0] - A[i][1]
                right = A[i][0] + A[i][1]
 
    print(N - cnt)

if __name__ == "__main__":
    main()