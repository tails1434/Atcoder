def main():
    N = int(input())
    if N == 0:
        print(0)
    ans = ''
    base = 1
    while N != 0:
        if N % (base * -2) == 0:
            ans += '0'
        else:
            ans += "1"
            N -= base
        base *= -2
    ans = list(ans)
    ans.reverse()
    print(''.join(ans))

if __name__ == "__main__":
    main()