from collections import defaultdict

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    for _ in range(M):
        B, C = map(int, input().split())
        d[C] += B

    sort_d = sorted(d.items(),reverse = True)

    cnt = 0
    ans = 0
    for i,j in sort_d:
        if cnt + j < N:
            ans += i * j
            cnt += j
        elif cnt + j >= N:
            if cnt == N:
                break
            ans += i * (N - cnt)
            break 

    print(ans)



main()