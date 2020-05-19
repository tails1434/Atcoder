import math
from decimal import Decimal

def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

def main():
    A, B, H, M = map(int, input().split())
    deg_H = (360 // 12) * H + 0.5 * M
    deg_M = (360 // 60) * M
    
    x_A = A * Decimal(math.sin(math.radians(deg_H)))
    y_A = A * Decimal(math.cos(math.radians(deg_H)))
    x_B = B * Decimal(math.sin(math.radians(deg_M)))
    y_B = B * Decimal(math.cos(math.radians(deg_M)))
    
    ans = float((Decimal(x_A) - Decimal(x_B)) ** 2 + (Decimal(y_A) - Decimal(y_B)) ** 2) ** 0.5
    print(ans)




if __name__ == "__main__":
    main()