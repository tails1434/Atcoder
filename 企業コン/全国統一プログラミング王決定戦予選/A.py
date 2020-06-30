def main():
    N, A, B = map(int, input().split())
    mx = min(A,B)
    mi = max((A + B) - N,0)
    print(mx,mi)


if __name__ == "__main__":
    main()