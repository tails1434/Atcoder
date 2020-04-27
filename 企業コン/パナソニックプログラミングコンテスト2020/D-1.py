def num_to_str(n):
    return chr(97 + n)

def str_to_num(s):
    return ord(s) - 97

def dfs(s,m,n,N,ans):
    if n == N:
        ans.append(s)
        return
    for i in range(m+2):
        dfs(s+num_to_str(i),max(m,i),n+1,N,ans)

def main():
    N = int(input())
    ans = []
    dfs('a',0,1,N,ans)
    ans.sort()
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
