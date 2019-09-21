def main():
    N = int(input())
    S = input()
    cnt = 0
    pre = 0
    for i in range(len(S)):
        if S[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                pre = max(pre, -cnt)
    
    ans = "(" * pre + S
    cnt = 0
    for j in range(len(ans)):
        if ans[j] == '(':
            cnt += 1
        else:
            cnt -= 1

    print(ans + ')' * cnt)

main()