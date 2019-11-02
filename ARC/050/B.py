def main():
    R, B = map(int, input().split())
    x, y = map(int, input().split())

    ok = 0
    ng = 10 ** 18
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if min(R, B) < mid:
            ng = mid
        else:
            pR = R - mid
            pB = B - mid
            if mid > pR // (x - 1) + pB // (y - 1):
                ng = mid
            else:
                ok = mid
    
    print(ok)

if __name__ == "__main__":
    main()