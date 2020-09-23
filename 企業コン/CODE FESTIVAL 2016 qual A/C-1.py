def main():
    S = list(input())
    K = int(input())
    L = len(S)
    for i in range(L):
        if S[i] == 'a':
            continue
        if ord('z') - ord(S[i]) + 1 <= K:
            K -= ord('z') - ord(S[i]) + 1
            S[i] = 'a'

    if K > 0:
        S[-1] = chr(ord(S[-1]) + K % 26)

    print(''.join(S))




if __name__ == "__main__":
    main()