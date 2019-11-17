def main():
    N = int(input())
    S = input()
    if N % 2 != 0:
        print('No')
    else:
        A = S[:N//2]
        B = S[N//2:N]
        if A == B:
            print('Yes')
        else:
            print('No')

  

if __name__ == "__main__":
    main()