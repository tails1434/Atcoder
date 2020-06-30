def main():
    S = input()
    gu = 0
    par = 0
    ans = 0
    for s in S:
        if s == 'g':
            if par < gu:
                ans += 1
                par += 1
            else:
                gu += 1
        else:
            if par < gu:
                par += 1
            else:
                ans -= 1
                gu += 1

    print(ans)



if __name__ == "__main__":
    main()