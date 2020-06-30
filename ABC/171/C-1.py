
def main():
    N = int(input())
    ans = ''
    keta = 1
    tmp = 0
    while N > 0:
        cnt = N % 26
        if cnt == 0:
            cnt = 26
            N -= 1
        ans = chr(96+cnt) + ans
        N //= 26
    print(ans)

if __name__ == "__main__":
    main()