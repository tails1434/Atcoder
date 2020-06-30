def main():
    N, A, B, C, D = map(int, input().split())
    S = input()
    for i in range(A-1,D):
        if S[i] == '#' and S[i+1] == '#':
            print('No')
            exit()
    
    if C < D:
        print('Yes')
        exit()
    
    for i in range(B-1,D):
        if D != len(S):
            if S[i-1] == '.' and S[i] == '.' and S[i+1] == '.':
                print('Yes')
                exit()

    print('No')


if __name__ == "__main__":
    main()
