def main():
    N, R = map(int, input().split())
    S = list(input())
    ans = 0
    cnt = 0
    c = S.count('.')
    while c > 0:
        if c == S[cnt:min(cnt+R,N)].count('.'):
            ans += 1
            break
        else:
            if S[cnt] == '.':
                for i in range(cnt, cnt+R):
                    S[i] = 'o'
                c = S.count('.')
            else:
                cnt += 1
        ans += 1

    print(ans)


            


if __name__ == "__main__":
    main()