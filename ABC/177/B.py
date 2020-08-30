def main():
    S = list(input())
    T = list(input())
    ans = float('inf')
    for i in range(len(S)):
        cnt = 0
        flag = True
        for j in range(len(T)):
            if i + j >= len(S):
                flag = False
                break
            if S[i+j] != T[j]:
                cnt += 1
        if flag:
            ans = min(ans, cnt)

    print(ans)




if __name__ == "__main__":
    main()