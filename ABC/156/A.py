def main():
    N, R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        ans = R + 100 * (10 - N)
        print(ans)




if __name__ == "__main__":
    main()