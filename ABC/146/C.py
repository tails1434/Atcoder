def main():
    A, B, X = map(int, input().split())
    cnt = 0
    for i in range(10):
        tmp_N = 10 ** i
        if A * tmp_N + B * (i+1) > X:
            cnt = i
            break
    else:
        print(10 ** 9)
        exit()
    if cnt == 0:
        print(0)
        exit()
    
    N = (X - (B * cnt)) // A
    if len(str(N)) != cnt:
        print('9' * cnt)
    else:
        print(N)




if __name__ == "__main__":
    main()
