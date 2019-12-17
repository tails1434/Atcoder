def main():
    N = int(input())
    S = input()

    left = 0
    right = 0
    for s in S:
        if s == '(':
            right += 1
        else:
            if right <= 0:
                left += 1
            else:
                right -= 1

    ans = left * '(' + S + right * ')'
    print(ans)


if __name__ == "__main__":
    main()