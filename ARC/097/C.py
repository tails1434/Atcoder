def main():
    S = input()
    K = int(input())
    ans = []
    def dfs(s,cnt):
        res = cnt 
        if len(s) > K:
            return
        for i in range(97,123):
            tmp = s + chr(i)
            if tmp in S:
                ans.append(tmp)
                if res == K:
                    return
                dfs(tmp,res)

    
    dfs('',0)
    ans.sort()
    print(ans[K-1])



if __name__ == "__main__":
    main()