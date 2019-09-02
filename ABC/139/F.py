import math
from decimal import *


def main():
    N = int(input())

    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())

    ans = 0
    # +x,+yを考える
    ax = 0
    ay = 0
    for i in range(N):
        if x[i] >= 0 and y[i] >= 0:
            ax += x[i]
            ay += y[i]
        elif x[i] >= 0 and y[i] <= 0:
            if abs(x[i]**2) > abs(y[i]**2):
                ax += x[i]
                ay += y[i]
        elif x[i] <= 0 and y[i] >= 0:
            if abs(x[i]**2) < abs(y[i]**2):
                ax += x[i]
                ay += y[i]

    tmp = Decimal(math.sqrt(Decimal(Decimal(ax)**Decimal(2)) + Decimal(Decimal(ay)**Decimal(2))))
    ans = max(ans, tmp)

    # -x,+yを考える
    ax = 0
    ay = 0
    for i in range(N):
        if x[i] <= 0 and y[i] >= 0:
            ax += x[i]
            ay += y[i]
        elif x[i] >= 0 and y[i] >= 0:
            if abs(x[i]**2) < abs(y[i]**2):
                ax += x[i]
                ay += y[i]
        elif x[i] <= 0 and y[i] <= 0:
            if abs(x[i]**2) > abs(y[i]**2):
                ax += x[i]
                ay += y[i]

    tmp = Decimal(math.sqrt(Decimal(Decimal(ax)**Decimal(2)) + Decimal(Decimal(ay)**Decimal(2))))
    ans = max(ans, tmp)

    # -x,-yを考える
    ax = 0
    ay = 0
    for i in range(N):
        if x[i] <= 0 and y[i] <= 0:
            ax += x[i]
            ay += y[i]
        elif x[i] <= 0 and y[i] >= 0:
            if abs(Dx[i]**2) > abs(y[i]**2):
                ax += x[i]
                ay += y[i]
        elif x[i] >= 0 and y[i] <= 0:
            if abs(x[i]**2) < abs(y[i]**2):
                ax += x[i]
                ay += y[i]

    tmp = Decimal(math.sqrt(Decimal(Decimal(ax)**Decimal(2)) + Decimal(Decimal(ay)**Decimal(2))))
    ans = max(ans, tmp)

    # x,-yを考える
    ax = 0
    ay = 0
    for i in range(N):
        if x[i] >= 0 and y[i] <= 0:
            ax += x[i]
            ay += y[i]
        elif x[i] >= 0 and y[i] >= 0:
            if abs(x[i]**2) > abs(y[i]**2):
                ax += x[i]
                ay += y[i]
        elif x[i] <= 0 and y[i] <= 0:
            if abs(x[i]**2) < abs(y[i]**2):
                ax += x[i]
                ay += y[i]

    tmp = Decimal(math.sqrt(Decimal(Decimal(ax)**Decimal(2)) + Decimal(Decimal(ay)**Decimal(2))))
    ans = max(ans, tmp)

    print(ans)

main()