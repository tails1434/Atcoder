def main():
    A: int
    B: int
    C: int
    D: int
    A, B, C, D = map(int, input().split())
    if A <= C <= B or C <= A <= D:
        print('Yes')
    else:
        print('No')




if __name__ == "__main__":
    main()