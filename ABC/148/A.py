def main():
    A = [int(input()) for _ in range(2)]
    num = [1,2,3]
    for n in num:
        if not n in A:
            print(n)
            exit()



if __name__ == "__main__":
    main()