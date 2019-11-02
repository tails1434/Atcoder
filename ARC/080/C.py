from collections import defaultdict
def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 4 == 0:
                d[2] += 1
            else:
                d[1] += 1
        else:
            d[0] += 1
    
    if d[1] == 0:
        if d[0] - 1 <= d[2]:
            print('Yes')
            exit()
    else:
        if d[0] <= d[2]:
            print('Yes')
            exit()

    print('No')

    


if __name__ == "__main__":
    main()