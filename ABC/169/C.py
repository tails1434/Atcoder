import math
from decimal import Decimal

def main():
    A, B = input().split()
    ans = Decimal(A) * Decimal(B)
    print(math.floor(ans))



if __name__ == "__main__":
    main()