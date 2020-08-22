def main():
    N = 1000 - int(input())
    ans = 0

    while N // 500 != 0:
        N -= 500
        ans += 1
    while N // 100 != 0:
        N -= 100
        ans += 1
    
    while N // 50 != 0:
        N -= 50
        ans += 1
    while N // 10 != 0:
        N -= 10
        ans += 1
    while N // 5 != 0:
        N -= 5
        ans += 1
    ans += N
    print(ans)



if __name__ == "__main__":
    main()