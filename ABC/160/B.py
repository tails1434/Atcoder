def main():
    X = int(input())
    cnt_500 = X // 500
    cnt_5 = (X - 500 * cnt_500) // 5
    ans = cnt_500 * 1000 + cnt_5 * 5
    print(ans)





if __name__ == "__main__":
    main()