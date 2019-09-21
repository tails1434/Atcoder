import heapq
def func(n):
    return -n

def main():
    N, M = map(int, input().split())
    A = list(map(func, map(int, input().split())))

    heapq.heapify(A)

    for _ in range(M):
        tmp = -heapq.heappop(A) // 2
        heapq.heappush(A,-tmp)

    print(-sum(A))

main()