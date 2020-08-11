def main():
    S = input()
    s = set()
    for i in range(2**len(S)):
        tmp = S[0]
        for j in range(1,len(S)):
            if (i >> j) & 1:
                tmp += '+' + S[j]
            else:
                tmp += S[j]
        s.add(tmp)
    ans = 0
    for a in s:
        ans += eval(a)
    print(ans)



if __name__ == "__main__":
    main()