def runlength(S):
    cnt = 1
    d = []
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            d.append(cnt)
            cnt = 1
    else:
        d.append(cnt)

    return d



def main():
    N = int(input())
    S = input()
    d = runlength(S)
    print(len(d))

  

if __name__ == "__main__":
    main()