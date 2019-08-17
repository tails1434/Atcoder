def main():
    c = [[0] * 3] * 3

    for i in range(3):
        c[i] = list(map(int, input().split()))

    if (c[0][0] - c[1][0]) == (c[0][1] - c[1][1]) == (c[0][2] - c[1][2]):
        if (c[1][0] - c[2][0]) == (c[1][1] - c[2][1]) == (c[1][2] - c[2][2]):
            if (c[0][0] - c[2][0]) == (c[0][1] - c[2][1]) == (c[0][2] - c[2][2]):
                print('Yes')
                exit()
    print('No')

main()