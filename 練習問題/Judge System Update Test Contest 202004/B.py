def main():
    N = int(input())
    red = []
    blue = []
    for _ in range(N):
        X, C = input().split()
        if C == 'R':
            red.append(int(X))
        else:
            blue.append(int(X))

    red.sort()
    blue.sort()
    for r in red:
        print(r)
    for b in blue:
        print(b)


    


if __name__ == "__main__":
    main()