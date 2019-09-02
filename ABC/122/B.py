def main():
    S = input()

    word = ['A','C','G','T']
    ans = 0
    cnt = 0
    for s in S:
        if s in word:
            cnt += 1
            ans = max(ans,cnt)
        else:
            cnt = 0

    print(ans)



main()