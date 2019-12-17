def divisor(n):
    ass = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ass.append(i)

            if i ** 2 == n:
                continue
            ass.append(n // i)
    return ass

def main():
    N, M = map(int, input().split())
    d = divisor(M)
    d.sort(reverse=True)
    for i in d:
        if i * N <= M:
            print(i)
            exit()




if __name__ == "__main__":
    main()