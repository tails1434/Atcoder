N = int(input())

def dfs(n,i,s,ans):
    if n == N:
        ans.append(s)
        return
    
    for j in range(i+1):
        tmp = s + chr(j + 97)
        max_j = ord(max(tmp)) - 96
        dfs(n+1,max_j,tmp,ans) 
    

def main():
    ans = []
    dfs(1,1,'a',ans)
    ans.sort()
    for a in ans:
        print(a)


    


if __name__ == "__main__":
    main()