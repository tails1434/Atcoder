from bisect import bisect_right
from itertools import accumulate

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()
    B_count = [0] * N
    for i in range(N):
        index = bisect_right(C,B[i])
        if index < N:
            B_count[i] = N - index
    D = [0] + list(accumulate(B_count))
    ans = 0
    for a in A:
        index = bisect_right(B,a)
        ans += D[N] - D[index]

    print(ans)

if __name__ == "__main__":
    main()