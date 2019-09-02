def main():
    A, B, T = map(int, input().split())

    cnt = 0
    for i in range(1, 100):
        if T + 0.5 >= A * i:
            cnt += 1
        else:
            print(cnt*B)
            exit()

main()