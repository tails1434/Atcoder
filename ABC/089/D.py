def main():
    H, W, D = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(H)]

    c = [0] * (H * W)
    for i in range(H):
        for j in range(W):
            c[field[i][j] - 1] = (i, j)
    
    d = [0] * (H * W)
    for l in range(H * W - D):
        i, j = c[l]
        x, y = c[l + D]
        d[l+D] = d[l] + abs(x - i) + abs(y - j)
    
    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        print(d[R-1]-d[L-1])


main()

##from functools import lru_cache
##
##def main():
##    @lru_cache(maxsize=1000)
##    def dfs(d,R,sx,sy):
##        if d == R:
##            return 0
##        x = 0
##        y = 0
##        for i in range(H):
##            for j in range(W):
##                if A[i][j] == d + D:
##                    x = i
##                    y = j
##                    break
##            else:
##                continue
##            break
##        
##        res = abs(x - sx) + abs(y - sy) + dfs(d+D,R,x,y)
##
##        return res
##    
##    H, W, D = map(int, input().split())
##    A = [list(map(int, input().split())) for _ in range(H)]
##    Q = int(input())
##
##    for _ in range(Q):
##        L, R = map(int, input().split())
##        sx = 0
##        sy = 0
##        for i in range(H):
##            for j in range(W):
##                if A[i][j] == L:
##                    sx = i
##                    sy = j
##                    break
##            else:
##                continue
##            break
##        print(dfs(L,R,sx,sy))
##
##        
##        
##        
##
##main()