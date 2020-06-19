def main():
    S = input()
    len_S = len(S)
    if S == '{}':
        print('dict')
        exit()

    left = 0
    right = 0
    for i in range(len_S):
        if S[i] == '{':
            left += 1
        if S[i] == '}':
            right += 1
        
        if left - right == 1:
            if S[i] == ':':
                print('dict')
                exit()
    else:
        print('set')

if __name__ == "__main__":
    main()
