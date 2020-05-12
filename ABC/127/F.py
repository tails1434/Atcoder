import sys
input = sys.stdin.readline
import heapq 

def main():
    Q = int(input())
    ans = 0
    l = []
    r = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            ans += query[2]
            heapq.heappush(l, -query[1])
            heapq.heappush(r, query[1])
            if -l[0] > r[0]:
                l_max = -1 * heapq.heappop(l)
                r_min = heapq.heappop(r)
                ans += abs(l_max-r_min)
                heapq.heappush(l, -r_min)
                heapq.heappush(r, l_max)

        else:
            print(-l[0],ans)


if __name__ == "__main__":
    main()