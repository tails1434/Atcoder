from bisect import bisect_left
from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    sushi = []
    child = deque([])
    flag = True
    for i in range(M):
        if flag and len(child) == N:
            flag = False
        index = bisect_left(child, A[i])
        if index == 0:
            if flag:
                child.appendleft(A[i])
                print(len(child))
            else:
                print(-1)
        else:
            child[index-1] = A[i]
            sushi.append(abs(index - 1 - len(child)))
            print(abs(index - 1 - len(child)))

if __name__ == "__main__":
    main()