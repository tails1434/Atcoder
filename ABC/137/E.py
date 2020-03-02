from collections import deque
import sys
input = sys.stdin.readline


def main():
    N, M, P = map(int, input().split())
    edge = []
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        C -= P
        C = -C
        edge.append((A,B,C))
        g[A].append(B)
        rg[B].append(A)

    # 0 => N-1の間にある閉路を検出したいので
    # 0とN-1からたどりつけない場所は前処理で取り除く
    
    visited1 = set() 
    visited2 = set()
    visited1.add(0)
    visited2.add(N-1)
    Q = deque()
    Q.append(0)
    while Q:
        v = Q.popleft()
        for dest in g[v]:
            if dest in visited1:
                continue
            visited1.add(dest)
            Q.append(dest)
    
    Q.append(N-1)
    while Q:
        v = Q.popleft()
        for dest in rg[v]:
            if dest in visited2:
                continue
            visited2.add(dest)
            Q.append(dest)
    
    OK = visited1 & visited2
    
    flag = True
    d = [float('inf')] * N
    d[0] = 0
    step = 0
    while flag:
        flag = False
        for A, B, C in edge:
            if not A in OK:
                continue
            if not B in OK:
                continue
            newD = d[A] + C
            if newD < d[B]:
                d[B] = newD
                flag = True
        step += 1
        if step > N:
            print(-1)
            exit()
 
    print(max(0,-d[N-1]))


if __name__ == "__main__":
    main()