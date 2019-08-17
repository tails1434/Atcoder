def main():
    S = input()
    K = int(input())

    cnt = 0
    for s in S:
        if s == '1':
            cnt += 1
            if K == cnt:
                print(1)
                exit()
        else:
            print(s)
            exit()



main()