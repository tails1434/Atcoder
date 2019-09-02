def main():
    S = input()

    if 1 <= int(S[0]+S[1]) <= 12 and 1 <= int(S[2]+S[3]) <= 12:
        print('AMBIGUOUS')
    elif 1 <= int(S[0]+S[1]) <= 12:
        print('MMYY')
    elif 1 <= int(S[2]+S[3]) <= 12:
        print('YYMM')
    else:
        print('NA')

main()