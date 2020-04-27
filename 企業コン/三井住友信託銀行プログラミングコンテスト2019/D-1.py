def main():
    N = int(input())
    S = list(map(int,list(input())))
    ans = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                cnt = 0
                for n in range(N):
                    if cnt == 0 and S[n] == i:
                        cnt += 1
                    elif cnt == 1 and S[n] == j:
                        cnt += 1
                    elif cnt == 2 and S[n] == k:
                        cnt += 1
                    
                    if cnt == 3:
                        ans += 1
                        break
    print(ans)
    
if __name__ == "__main__":
    main()