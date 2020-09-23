def main():
    A, B, C, D, E, F = map(int, input().split())
    ans = -1
    sugar = 0
    sugar_water = 0
    for a in range(F // (A * 100) + 1):
        for b in range((F - 100 * A * a) // (B * 100) + 1):
            for c in range((F - 100 * A * a - 100 * B * b) // C + 1):
                for d in range((F - 100 * A * a - 100 * B * b - C * c) // D + 1):
                    x = a * A + b * B
                    y = c * C + d * D
                    if x == 0:
                        continue
                    if x * E >= y and ans < (100 * y)/(x*100+y):
                        ans = (100 * y)/(x*100+y)
                        sugar = y
                        sugar_water = 100 * x + y
    print(sugar_water,sugar)

if __name__ == "__main__":
    main()