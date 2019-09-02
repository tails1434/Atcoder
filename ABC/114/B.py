def main():
    S = input()
    X = 753

    ans = float('inf')
    for i in range(len(S)-2):
        tmp = int(S[i] + S[i+1] + S[i+2])
        if ans > abs(X - tmp):
            ans = abs(X - tmp)

    print(ans)
main()