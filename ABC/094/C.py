def main():
    N = int(input())
    X = list(map(int, input().split()))

    sort_X = sorted(X)
    X1 = sort_X[N//2]
    X2 = sort_X[(N//2) - 1]

    for x in X:
        if x <= X2:
            print(X1)
        else:
            print(X2)
main()