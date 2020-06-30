def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    ass.sort()
    return ass #sortされていない


def main():
    N = int(input())
    if N <= 2:
        print(0)
        exit()
    ans = 0
    for i in divisor(N):
        if i == 1:
            continue
        if N // (i-1) == N % (i-1):
            ans += (i-1)

    print(ans)

if __name__ == "__main__":
    main()