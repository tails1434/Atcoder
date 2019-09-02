def main():
    N, T = map(int, input().split())

    ans = float('inf')

    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            if ans > c:
                ans = c

    if ans == float('inf'):
        print('TLE')
    else:
        print(ans)

main()