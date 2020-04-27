from collections import defaultdict

def main():
    X, Y, A, B, C = map(int, input().split())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    R = list(map(int, input().split()))
    d_p = defaultdict(int)
    d_q = defaultdict(int)
    d_r = defaultdict(int)
    for p in P:
        d_p[p] += 1
    for q in Q:
        d_q[q] += 1
    for r in R:
        d_r[r] += 1
    D = P + Q + R
    D.sort(reverse=True)
    ans = 0
    x = 0
    y = 0
    c = 0
    for i in range(A + B + C):
        if x + y + c >= X + Y:
            break

        if x < X and d_p[D[i]]:
            ans += D[i]
            x += 1
            d_p[D[i]] -= 1
        elif y < Y and d_q[D[i]]:
            ans += D[i]
            y += 1
            d_q[D[i]] -= 1
        elif d_r[D[i]]:
            ans += D[i]
            c += 1
            d_r[D[i]] -= 1

    print(ans)

if __name__ == "__main__":
    main()