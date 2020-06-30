
ans = []

def dfs(i,keta,s):
    if i == keta:
        ans.append(s)
        return
    
    for j in range(26):
        ret = s + chr(97+j)
        dfs(i+1,keta,ret)


def main():
    #N = int(input())
    N = 1000000000000001
    cnt = 26
    keta = 2
    while N >= 0:
        if N - cnt <= 0:
            break
        N -= cnt
        cnt = 26 ** keta
        keta += 1
    
    print(keta-1,N)
    #dfs(0,keta-1,'')
    #print(ans)

if __name__ == "__main__":
    main()