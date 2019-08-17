def main():
    N = int(input())


    d = [0] * N

    for i in range(N):
        d[i] = int(input())

    set_d = set(d)

    print(len(set_d))

main()