def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    A = [a,b,c,d,e]
    for i in range(len(A)):
        for j in range(i,len(A)):
            if A[j] - A[i] > k:
                print(':(')
                exit()

    print('Yay!')

main()