def main():
    N = int(input())

    W = [""] * N

    for i in range(N):
        W[i] = input()

    set_W = set(W)

    if len(set_W) != N:
        print('No')
        exit()

    for i in range(N-1):
        if W[i][len(W[i]) - 1] != W[i+1][0]:
            print('No')
            exit()

    print('Yes')


main()