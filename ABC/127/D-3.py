from collections import defaultdict

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    d =  defaultdict(int)
    for a in A:
        d[a] += 1

    for _ in range(M):
        B, C = map(int, input().split())
        d[C] += B

    ans = 0

    cand = list(d.keys())
    cand.sort(reverse=True)
    cnt = 0
    for c in cand:
        if cnt + d[c] <= N:
            ans += c * d[c]
            if cnt + d[c] == N:
                break
            cnt += d[c]
        else:
            ans += c * (N - cnt)
            break

    print(ans)
        


if __name__ == "__main__":
    main()