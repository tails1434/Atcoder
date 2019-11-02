import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    keys = []
    for i in range(M):
        a, b = map(int, input().split())
        s = 0
        C = list(map(int, input().split()))
        for c in C:
            c -= 1
            s |= 1 << c
        keys.append([s,a])

    dp = [float('inf')] * (1 << N)

    dp[0] = 0
    for s in range(1 << N):
        for i in range(M):
            t = s | keys[i][0]
            cost = dp[s] + keys[i][1]
            dp[t] = min(dp[t],cost)
    
    if dp[-1] == float('inf'):
        print(-1)
    else:
        print(dp[-1])
            
main()