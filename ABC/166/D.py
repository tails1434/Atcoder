def main():
    X = int(input())
    for A in range(10**7):
        tmp = pow(A,5) - X
        if tmp == 0:
            print(A,0)
            exit()
        elif tmp < 0:
            for i in range(-1,-(10**7),-1):
                if tmp == pow(i,5) and pow(A,5) - pow(i,5) == X:
                    print(A,i)
                    exit()
                elif tmp > pow(i,5):
                    break
        else:
            for i in range(1,10**7):
                if tmp == pow(i,5) and pow(A,5) - pow(i,5) == X:
                    print(A,i)
                    exit()
                elif tmp < pow(i,5):
                    break



if __name__ == "__main__":
    main()