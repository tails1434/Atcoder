def main():
    n, m, d = map(int, input().split())
    if d == 0:
        ans = (m-1) / n
    else:
        ans =  2 * (m-1) * (n-d) / n ** 2

    print(ans)





if __name__ == "__main__":
    main()