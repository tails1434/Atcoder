import sys
from collections import deque
from itertools import accumulate
from bisect import bisect_right

sys.setrecursionlimit(4100000)

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [0] + list(accumulate(A))
    D = [0] + list(accumulate(B))
    if sum(A) + sum(B) <= K:
        print(N+M)
        exit()
    
    cnt = 0
    for i in range(N+1):
        tmp_cnt = i
        tmp_ans = C[i]
        if tmp_ans > K:
            break
        tmp_index = bisect_right(D, K-tmp_ans) -1
        tmp_cnt += tmp_index
        cnt = max(cnt,tmp_cnt)



    print(cnt)





if __name__ == "__main__":
    main()