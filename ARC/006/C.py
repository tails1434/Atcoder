from collections import deque
from bisect import bisect_left

def main():
    N = int(input())
    W = [int(input()) for _ in range(N)]
    q = deque([W[0]])

    for i in range(1,N):
        index = bisect_left(q,W[i])
        if q[-1] < W[i]:
            q.append(W[i])
        else:
            q[index] = W[i]
    
    print(len(q))




if __name__ == "__main__":
    main()