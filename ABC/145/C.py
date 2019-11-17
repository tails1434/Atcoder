from itertools import permutations
from decimal import *
import math

def main():
    N = int(input())
    X = [] 
    for i in range(N):
        x, y = map(int, input().split())
        X.append((x,y))

    ans = 0

    for A in permutations(X):
        tmp = 0
        i = 0
        pre_x = 0
        pre_y = 0
        for x, y in A:
            if i == 0:
                pre_x = x
                pre_y = y
                i += 1
            else:
                tmp = (x - pre_x) ** 2 + (y - pre_y) ** 2
                ans += tmp ** 0.5
                i += 1 
    
    ans = Decimal(ans) / Decimal(math.factorial(N))
    print(ans)




  

if __name__ == "__main__":
    main()