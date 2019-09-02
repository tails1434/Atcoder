def main():
    A = list(map(int,input().split()))

    A.remove(max(A))

    print(int(A[0]*A[1]/2))


main()