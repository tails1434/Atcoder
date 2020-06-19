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
    N = int(input())
    div = divisor(N)
    if N == sum(div) - N:
        print('Perfect')
    elif N < sum(div) - N:
        print('Abundant')
    else:
        print('Deficient')


if __name__ == "__main__":
    main()