def main():
    N = int(input())
    C = []
    for i in range(N):
        A, B = map(int, input().split())
        C.append([B,A])

    sort_C = sorted(C)

    s = 0
    for c in sort_C:
        if s + c[1] <= c[0]:
            s += c[1]
        else:
            print('No')
            exit()

    print('Yes')

main()