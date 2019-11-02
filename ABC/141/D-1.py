import heapq

def func(x):
    return -x

def main():
    N, M = map(int, input().split())
    A = list(map(func, map(int, input().split())))
    heapq.heapify(A)

    for _ in range(M):
        tmp = heapq.heappop(A)
        heapq.heappush(A, -(-tmp//2))

    print(-sum(A))



if __name__ == "__main__":
    main()