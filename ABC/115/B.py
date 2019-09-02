def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    
    ans = 0
    max_p = max(p)
    flag = False
    for i in p:
        if i == max_p and flag == False:
            ans += i // 2
            flag = True
        else:
            ans += i

    print(ans)

main()