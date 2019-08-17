def main():
    N = int(input())
    A = list(map(int, input().split()))

    sort_A = sorted(A, reverse=True)
    alice = 0
    bob = 0
    for i, a in enumerate(sort_A):
        if i % 2 == 0:
            alice += a
        else:
            bob += a

    print(alice - bob)


main()