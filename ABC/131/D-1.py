def main():
    N = int(input())
    A = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append((b,a))

    A.sort()
    time = 0
    for b, a in A:
        time += a
        if time > b:
            print('No')
            exit()

    print('Yes')    



if __name__ == "__main__":
    main()