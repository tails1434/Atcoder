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
    S = int(input())
    X1, Y1 = 0, 0
    Y2 = 1
    X2 = 10 ** 9
    Y3 = S // X2 if S % X2 == 0 else S // X2 + 1
    X3 = (10 ** 9) * Y3 - S


    print(X1,Y1,X2,Y2,X3,Y3)




if __name__ == "__main__":
    main()