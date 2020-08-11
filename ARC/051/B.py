def main():
    K = int(input())
    a = 1
    b = 1
    for i in range(K-1):
        a, b = b, a + b

    print(a,b)

if __name__ == "__main__":
    main()