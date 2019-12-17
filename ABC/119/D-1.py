from bisect import bisect_left

def main():
    A, B, Q = map(int, input().split())
    S = [0] * A
    T = [0] * B
    for i in range(A):
        S[i] = int(input())
    for i in range(B):
        T[i] = int(input())
    
    for _ in range(Q):
        x = int(input())
        s_cnt = bisect_left(S,x)
        t_cnt = bisect_left(T,x)
        s_cand = []
        t_cand = []
        if s_cnt == 0:
            s_cand.append(S[s_cnt])
        elif s_cnt == A:
            s_cand.append(S[s_cnt-1])
        else:
            s_cand.append(S[s_cnt])
            s_cand.append(S[s_cnt-1])
        if t_cnt == 0:
            t_cand.append(T[t_cnt])
        elif t_cnt == B:
            t_cand.append(T[t_cnt-1])
        else:
            t_cand.append(T[t_cnt])
            t_cand.append(T[t_cnt-1])
        d = float('inf')
        for i in s_cand:
            for j in t_cand:
                tmp = abs(x - i) + abs(i - j)
                d = min(d, tmp)

        for i in t_cand:
            for j in s_cand:
                tmp = abs(x - i) + abs(i - j)
                d = min(d, tmp)
        print(d)


if __name__ == "__main__":
    main()