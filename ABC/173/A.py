def main():
    N = int(input())
    div = N // 1000 if N % 1000 == 0 else N // 1000 + 1
    print(div * 1000 - N)

if __name__ == "__main__":
    main()