def main():
    N = int(input())

    S = list(input().split())

    set_S = set(S)

    if len(set_S) == 4:
        print('Four')
    else:
        print('Three')


main()