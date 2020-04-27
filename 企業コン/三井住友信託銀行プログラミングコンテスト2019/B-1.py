def main():
    N = int(input())
    for i in range(1,50000):
        if int(i * 1.08) == N:
            print(i)
            exit()
        
    print(':(')



if __name__ == "__main__":
    main()