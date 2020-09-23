def main():
    N, K = map(int, input().split())
    D = list(input().split())
    
    for i in range(N,100000):
        a = str(i)
        flag = True
        for d in D:
            if d in a:
                flag = False
                break
        if flag:
            print(i)
            exit()



if __name__ == "__main__":
    main()