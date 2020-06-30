def main():
    N, R = map(int, input().split())
    S = list(input())

    if S.count('.') == 0:
        print(0)
        exit()

    mx = 0
    for i in range(len(S)):
        if S[i] == '.':
            mx = i
    ans = 0
    index = 0
    cnt = 0
    while index < mx - R + 1:
        if S[index] == '.':
            cnt += 1
            for j in range(index, index+R):
                S[j] = 'o'
            
        index += 1
        cnt += 1
    print(cnt+1)
if __name__ == "__main__":
    main()