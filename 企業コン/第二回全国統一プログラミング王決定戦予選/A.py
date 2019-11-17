def main():
    N = int(input())
    num_list = set()
    for i in range(1,N+1):
        tmp = N - i
        if i == tmp or tmp == 0:
            continue
        else:
            num_list.add((i,tmp))

    if len(num_list) % 2 == 0:
        print(len(num_list) // 2)
    else:
        print(len(num_list) // 2 + 1)



if __name__ == "__main__":
    main()