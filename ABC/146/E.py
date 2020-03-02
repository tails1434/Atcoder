from itertools import accumulate
from collections import deque
from collections import defaultdict

def func(x):
    return x - 1

def main():
    N, K = map(int, input().split())
    A = list(map(func, map(int, input().split())))
    B = [0] + list(accumulate(A))
    for i in range(N+1):
        B[i] %= K

    Q = deque()
    d = defaultdict(int)
    ans = 0
    for i in range(N+1):
        ans += d[B[i]]
        d[B[i]] += 1
        Q.append(B[i])
        if len(Q) == K:
            a = Q.popleft()
            d[a] -= 1

    print(ans)


    


if __name__ == "__main__":
    main()