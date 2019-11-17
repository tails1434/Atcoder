from heapq import heappush, heappop
from collections import defaultdict
import copy

def main():
    N, T = map(int, input().split())
    d = defaultdict(list)
    C = []
    for i in range(N):
        A, B = map(int, input().split())
        C.append((A,B))
        d[A].append(B)

    num_list = []
    ans = 0
    for i in range(N):
        tmp = C[i][1]
        dp = [0] * T
        dp[T - 1] = tmp
        for i in range(T-1,-1,-1):
            

    print(ans)
    


    

if __name__ == "__main__":
    main()