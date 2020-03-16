def main():
    A, B = map(int, input().split())
    for i in range(1, 2000):
        tmp_A = int(i * 0.08)
        tmp_B = int(i * 0.10)
        if tmp_A == A and tmp_B == B:
            print(i)
            exit()

    print(-1)



if __name__ == "__main__":
    main()