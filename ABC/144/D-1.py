import math
from decimal import *

def main():
    a, b, x = map(int, input().split())
    if Decimal(a) * Decimal(b) / Decimal(2) >= Decimal(x) / Decimal(a):
        
    else:
        c = Decimal(b) * Decimal(b) * Decimal(a)
        ans = math.degrees(math.atan(Decimal(c)/decimal(x)))
        print(90 - ans)


if __name__ == "__main__":
    main()