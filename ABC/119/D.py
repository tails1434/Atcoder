import bisect
import sys
input = sys.stdin.readline

def main():
    A, B, Q = map(int, input().split())
    s = list(int(input()) for _ in range(A))
    t = list(int(input()) for _ in range(B))

    sort_s = sorted(s)
    sort_t = sorted(t)
    for _ in range(Q):
        x = int(input())
        s_near = bisect.bisect_left(sort_s, x)
        t_near = bisect.bisect_left(sort_t, x)

        s_candidate = []
        t_candidate = []

        if s_near == 0:
            s_candidate.append(sort_s[s_near])
        elif s_near == A:
            s_candidate.append(sort_s[s_near-1])
        else:
            s_candidate.append(sort_s[s_near])
            s_candidate.append(sort_s[s_near-1])
        
        if t_near == 0:
            t_candidate.append(sort_t[t_near])
        elif t_near == B:
            t_candidate.append(sort_t[t_near-1])
        else:
            t_candidate.append(sort_t[t_near])
            t_candidate.append(sort_t[t_near-1])

        ans = float('inf')
        # sを先に訪れるパターンを考える
        for i in s_candidate:
            for j in t_candidate:
                tmp = abs(x - i) + abs(i - j)
                ans = min(ans, tmp)

        # tをさきに訪れるパターンを考える
        for k in t_candidate:
            for l in s_candidate:
                tmp = abs(x - k) + abs(k - l)
                ans = min(ans, tmp)

        print(ans)

main()