def main():
    N, M, X, Y = map(int, input().split())

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    max_x = max(x)
    min_y = min(y)

    for i in range(X+1, Y):
        if max_x < i and min_y >= i:
            print('No War')
            exit()

    print('War')

main()