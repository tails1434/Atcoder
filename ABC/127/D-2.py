from collections import defaultdict

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for i in range(M):
        B, C = map(int, input().split())
        d[C] += B
    
    for a in A:
        d[a] += 1

    ans = 0
    cnt = 0
    for i in sorted(d.keys(),reverse=True):
        if cnt + d[i] < N:
            ans += d[i] * i
            cnt += d[i]
        else:
            ans += i * (N - cnt)
            cnt = N
            break

    print(ans)



if __name__ == "__main__":
    main()