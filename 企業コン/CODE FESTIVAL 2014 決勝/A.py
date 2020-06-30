from decimal import Decimal

def main():
    s = input()
    ans = Decimal('50') / Decimal(s)
    print(ans)

if __name__ == "__main__":
    main()