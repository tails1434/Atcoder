from collections import deque
from bisect import bisect_left

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    d = deque([])
    for i in range(N):
        p = bisect_left(d, A[i])
        if p == 0:
            d.appendleft(A[i])
        else:
            d[p-1] = A[i]

    print(len(d))


if __name__ == "__main__":
    main()