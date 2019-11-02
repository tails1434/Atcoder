def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    cnt = 0
    for i in range(N):
        if A[i] < 0:
            cnt += 1
        B[i] = abs(A[i])

    if cnt % 2 == 0:
        print(sum(B))
    else:
        print(sum(B) - 2 * min(B))

main()