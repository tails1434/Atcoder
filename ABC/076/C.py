def main():
    S = input()
    T = input()
    t = len(T)
    for i in range(len(S) - t, -1, -1):
        for j in range(t):
            if S[i + j] != T[j] and S[i + j] != '?':
                break
        else:
            print((S[:i] + T + S[i + t:]).replace("?","a"))
            exit()

    print("UNRESTORABLE")
main()