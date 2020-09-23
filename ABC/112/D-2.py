#nの約数列挙
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass #sortされていない


def main():
    N, M = map(int, input().split())
    ass = divisor(M)
    ass.sort()
    ans = 1
    for a in ass:
        if a <= (M // N):
            ass = a
        else:
            print(ass)
            exit()
    print(ass)

if __name__ == "__main__":
    main()