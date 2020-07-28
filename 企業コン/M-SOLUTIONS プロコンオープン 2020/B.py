def main():
    A, B, C = map(int, input().split())
    K = int(input())
    if A < B < C:
        print('Yes')
        exit()
    cnt = 0
    while cnt <= K:
        if A >= B:
            B *= 2
            cnt += 1
        else:
            break

    if A < B < C and cnt <= K:
        print('Yes')
        exit()

    while cnt <= K:
        if B >= C:
            C *= 2
            cnt += 1
        else:
            break
 
    if A < B < C and cnt <= K:
        print('Yes')
        exit()
    print('No')


    

if __name__ == "__main__":
    main()