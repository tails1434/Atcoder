from bisect import bisect_left

def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    for _ in range(Q):
        ans = float('inf')
        x = int(input())
        s_i = bisect_left(S,x)
        t_i = bisect_left(T,x)
        Temple = []
        if s_i == 0:
            Shrine = [S[0]]
        elif s_i == A:
            Shrine = [S[-1]]
        else:
            Shrine = [S[s_i-1],S[s_i]]
        if t_i == 0:
            Temple = [T[0]]
        elif t_i == B:
            Temple = [T[-1]]
        else:
            Temple = [T[t_i-1],T[t_i]]
        for s in Shrine:
            for t in Temple:
                dist = abs(s - x) + abs(t-s)
                ans = min(ans, dist)
                dist = abs(t - x) + abs(s-t)
                ans = min(ans, dist)
        print(ans)





if __name__ == "__main__":
    main()