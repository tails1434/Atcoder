import heapq
from collections import defaultdict

def main():
    N, M = map(int, input().split())
    ans = 0
    d = defaultdict(list)
    for _ in range(N):
        A, B = map(int, input().split())
        d[A].append(-B)
    cand = []
    heapq.heapify(cand)
    for day in range(M-1,-1,-1):
        diff = M - day
        for money in d[diff]:
            heapq.heappush(cand, money)
        if cand:
            ans -= heapq.heappop(cand)

    print(ans)



if __name__ == "__main__":
    main()