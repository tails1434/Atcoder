def main():
    N =  int(input())
    cnt = 0
    for i in range(3, N + 1, 2):
        div = 0
        for j in range(1,i+1):
            if i % j == 0:
                div += 1
        if div == 8:
            cnt += 1

    print(cnt)


main()