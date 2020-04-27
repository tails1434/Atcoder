import sys
sys.setrecursionlimit(100000)

def dfs(n,s,ans):
    if n == 10:
        return
    
    for i in range(10):

        tmp = s + str(i)
        if check(tmp):
            ans.append(int(tmp))
            dfs(n+1,tmp,ans)


def check(s):
    if abs(int(s[-1])-int(s[-2])) > 1:
        return False
    return True 

def main():
    K = int(input())
    ans = [1,2,3,4,5,6,7,8,9]
    for i in range(1,10):
        dfs(1,str(i),ans)
    # いらないはずだけど念のためソート
    ans.sort()
    print(ans[K-1])

    


if __name__ == "__main__":
    main()