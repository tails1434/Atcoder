def check(n,A,B,X):
    if A * n + B * len(str(n)) <= X:
        return True
    else:
        return False

def main():
    A, B, X = map(int, input().split())

    ok = 0
    ng = 10 ** 9 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(mid,A,B,X):
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()