def main():
    N = int(input())
    a = list(map(int, input().split()))

    color = [False] * 8

    cnt = 0
    for i in a:
        if 1 <= i <= 399:
            color[0] = True
        elif 400 <= i <= 799:
            color[1] = True
        elif 800 <= i <= 1199:
            color[2] = True
        elif 1200 <= i <= 1599:
            color[3] = True
        elif 1600 <= i <= 1999:
            color[4] = True
        elif 2000 <= i <= 2399:
            color[5] = True
        elif 2400 <= i <= 2799:
            color[6] = True
        elif 2800 <= i <= 3199:
            color[7] = True
        elif 3200 <= i:
            cnt += 1
    if color.count(True) == 0:
        print(1, color.count(True) + cnt)
    else:
        print(color.count(True), color.count(True) + cnt)
    

main()
