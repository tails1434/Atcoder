def main():
    N = int(input())
    A = list(map(int, input().split()))
    len_A = len(set(A))
    if N == len_A:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()