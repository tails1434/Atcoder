def main():
    N = list(map(int,list(input())))
    ans = 0
    for n in N:
        ans += n
        ans %= 9
    
    if ans % 9 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()