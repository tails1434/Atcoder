def main():
    A, B, C = map(int, input().split())

    if A + B < C:
        print('No')
    else:
        print('Yes')

main()