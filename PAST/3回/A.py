def main():
    s = input()
    t = input()
    if s == t:
        print('same')
        exit()

    if s.upper() == t.upper():
        print('case-insensitive')
        exit()
    
    print('different')

if __name__ == "__main__":
    main()