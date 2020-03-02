from itertools import accumulate
from bisect import bisect_left

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(accumulate(A))
    ans = 0
    for i in range(N):
        ans += N - bisect_left(B, B[i] + K)

    print(ans)






if __name__ == "__main__":
    main()