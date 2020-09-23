def main():
    N = int(input())
    X = []
    a = -float('inf') # x + y の最大
    b = float('inf') # x + y の最小
    c = -float('inf') # x - y の最大
    d = float('inf') # x - y の最小
    e = -float('inf') # -x+yの最大
    f = float('inf') # -x + yの最小
    g = -float('inf') # -x - yの最大
    h = float('inf') # -x - yの最小

    for _ in range(N):
        x, y = map(int, input().split())
        a = max(a, x + y)
        b = min(b, x + y)
        c = max(c, x - y)
        d = min(d, x - y)
        e = max(e, -x + y)
        f = min(f, -x + y)
        g = max(g, -x - y)
        h = min(h, -x - y)
    ans = a - b
    ans = max(ans, c-d)
    ans = max(ans, e-f)
    ans = max(ans, g-h)
    print(ans)


if __name__ == "__main__":
    main()