def main():
    N = int(input())
    P = list(map(int, input().split()))    
    cnt = 0
    i = 0
    while i < N:
        if i + 1 == P[i]:
            if i == N - 1:
                cnt += 1
                i += 1
            else:
                if i + 2 == P[i+1]:
                    cnt += 1
                    i += 2
                else:
                    cnt += 1
                    i += 1
        else:
            i += 1

    print(cnt)

if __name__ == "__main__":
    main()