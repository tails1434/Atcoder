def main():
    L = int(input())
    B = [int(input()) for _ in range(L)]
    cnt = B[0]
    for i in range(1,L):
        cnt ^= B[i]
    
    if cnt != 0:
        print(-1)
        exit()

    ans = [0] * (L)
    for i in range(1,L):
        ans[i] = ans[i-1] ^ B[i-1]

    for a in ans:
        print(a)



if __name__ == "__main__":
    main()