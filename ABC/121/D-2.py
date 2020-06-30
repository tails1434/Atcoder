def main():
    A, B = map(int, input().split())
    bin_B = bin(B)[2:]
    if A != 0:
        A -= 1
    bin_A = bin(A)[2:]
    cnt = [0] * len(bin_B)
    for i in range(len(bin_B)):
        loop = 2 ** (i+1)
        mod = B % loop
        if mod >= loop // 2:
            mod -= loop // 2
            mod += 1
        else:
            mod = 0
        cnt[i] = mod
        cnt[i] += (B // loop) * (loop // 2)
    for i in range(len(bin_A)):
        loop = 2 ** (i+1)
        mod = (A) % loop
        if mod >= loop // 2:
            mod -= loop // 2
            mod += 1
        else:
            mod = 0
        cnt[i] -= mod
        cnt[i] -= ((A) // loop) * (loop // 2)


    ans = 0
    for i in range(len(bin_B)):
        if cnt[i] % 2 == 1:
            ans += 2 ** i

    print(ans)


    



if __name__ == "__main__":
    main()