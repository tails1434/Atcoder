from decimal import Decimal

def main():
    N, D = map(int, input().split())
    ans = 0
    for _ in range(N):
        X, Y = map(int, input().split())
        tmp = X ** 2 + Y ** 2
        if tmp <= D ** 2:
            ans += 1

    print(ans)




if __name__ == "__main__":
    main()