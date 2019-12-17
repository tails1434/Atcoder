from itertools import accumulate
from bisect import bisect_left

def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))

    B = list(accumulate(A))
    ans = float('inf')
    for i in range(1,N):
        C = B[i] - B[0]
        D = B[N] - B[i]
        tmp = abs(C - D)
        ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()