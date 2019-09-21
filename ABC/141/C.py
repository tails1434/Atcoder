from collections import defaultdict

def main():
    N, K, Q = map(int, input().split())
    d = defaultdict(int)
    for _ in range(Q):
        A = int(input())
        d[A] += 1

    for i in range(1,N+1):
        if K - (Q - d[i]) > 0:
            print('Yes')
        else:
            print('No')


main()