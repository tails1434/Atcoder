import heapq
from collections import defaultdict
def main():
    N, M = map(int, input().split())
    work = defaultdict(list)
    for _ in range(N):
        A, B = map(int, input().split())
        work[M-A].append(B)
    
    ans = 0
    num_list = []
    heapq.heapify(num_list)
    for i in range(M-1,-1,-1):
        if work[i]:
            for j in work[i]:
                heapq.heappush(num_list,-j)
        if num_list:
            ans -= heapq.heappop(num_list)

    print(ans)




if __name__ == "__main__":
    main()