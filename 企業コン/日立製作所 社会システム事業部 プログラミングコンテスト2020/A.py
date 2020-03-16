def main():
    S = input()
    len_S = len(S)
    cnt = S.count('hi')
    if cnt * 2 == len_S:
        print('Yes')
    else:
        print('No')
    

if __name__ == "__main__":
    main()