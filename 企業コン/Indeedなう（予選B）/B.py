def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print(-1)
        exit()
    if s == t:
        print(0)
        exit()

    s += s
    ans = float('inf')
    if t not in s:
        print(-1)
        exit() 
    for i in range(len(t)):
        for j in range(len(t)):
            if s[i+j] != t[j]:
                break
        else:
            ans = min(ans, len(t) - i)

    print(ans)




if __name__ == "__main__":
    main()