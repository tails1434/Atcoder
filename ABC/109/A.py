def main():
    A, B = map(int, input().split())

    for C in range(1,4):
        if A * B * C % 2 == 1:
            print('Yes')
            exit()
    
    print('No')


main()