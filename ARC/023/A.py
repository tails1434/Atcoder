def main():
    y = int(input())
    m = int(input())
    d = int(input())
    if m == 1 or m == 2:
        m += 12
        y -= 1
    now = 365 * 2014 + (2014 // 4) - (2014 // 100) + (2014 // 400) + (306*(5+1)//10) + 17 - 429
    q = 365 * y + (y // 4) - (y // 100) + (y // 400) + (306*(m+1)//10) + d - 429
    print(now-q)

if __name__ == "__main__":
    main()