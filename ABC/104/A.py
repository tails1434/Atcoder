def main():
    R = int(input())

    if 0 <= R < 1200:
        print('ABC')
    elif 1200 <= R < 2800:
        print('ARC')
    else:
        print('AGC')


main()