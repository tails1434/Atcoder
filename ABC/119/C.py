def dfs(depth):
    if depth == N:
        ans.append(cal(v))
        return
    for i in range(4):
        v[depth] = i
        dfs(depth+1) 

def cal(v):
    tmp = [0] * 3 
    for i in range(N):
        if v[i] == 0:
            tmp[0] += l[i]
        elif v[i] == 1:
            tmp[1] += l[i]
        elif v[i] == 2:
            tmp[2] += l[i]
    cnt = 0
    if v.count(0) > 1:
        cnt += v.count(0) - 1
    if v.count(1) > 1:
        cnt += v.count(1) - 1
    if v.count(2) > 1:
        cnt += v.count(2) - 1

    if v.count(0) == 0 or v.count(1) == 0 or v.count(2) == 0:
        return float('inf')
    diff = cnt * 10
    for i in range(3):
        diff += abs(A[i]-tmp[i])
    
    return diff
        
    
    

N, *A= map(int, input().split())
l = [int(input()) for _ in range(N)]
v = [-1] * N

ans = []

dfs(0)
print(min(ans))