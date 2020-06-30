from decimal import Decimal

def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        a, b, c, d, e = map(int, input().split())
        tmp = a + b + c + d
        tmp += Decimal(str(e)) * Decimal(str(110)) / Decimal(str(900))
        ans = max(ans, tmp)

    print(ans)



if __name__ == "__main__":
    main()