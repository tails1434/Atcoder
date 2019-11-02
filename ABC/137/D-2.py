from collections import defaultdict
import heapq

def main():
    N, M = map(int, input().split())
    d = defaultdict(list)
    for _ in range(N):
        A, B = map(int, input().split())
        d[A].append(B)

    num_list = []
    heapq.heapify(num_list)
    ans = 0
    for i in range(1,M+1):
        if d[i]:
            for j in d[i]:
                heapq.heappush(num_list,-j)
        
        if num_list:
            ans -= heapq.heappop(num_list)

    print(ans)

    


main()