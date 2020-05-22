def main():
    N = int(input())
    work = []
    for _ in range(N):
        A, B = map(int, input().split())
        work.append((B,A))

    work.sort()
    
    time = 0
    for b, a in work:
        if b < time + a:
            print('No')
            exit()
        time += a
    print('Yes')

    



if __name__ == "__main__":
    main()