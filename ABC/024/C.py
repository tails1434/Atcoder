def main():
    N, D, K = map(int, input().split())
    L = [0] * D
    R = [0] * D
    for i in range(D):
        L[i], R[i] = map(int, input().split())
    
    for _ in range(K):
        S, T = map(int, input().split())
        now = S
        ans = 0
        if S < T:
            for i in range(D):
                if L[i] <= now:
                    now = max(now, R[i])
                    if now >= T:
                        print(i+1)
                        break
        else:
            for i in range(D):
                if R[i] >= now:
                    now = min(now, L[i])
                    if now <= T:
                        print(i+1)
                        break


if __name__ == "__main__":
    main()