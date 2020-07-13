from collections import deque

def main():
    S = list(input())
    ans = float('inf')
    for i in range(97,123):
        tmp = deque(S)
        cnt = 0
        s = chr(i)
        while len(tmp) > tmp.count(s):
            for j in range(len(tmp)):
                if tmp[j] == s:
                    continue
                if j + 1 < len(tmp) and tmp[j+1] == s:
                    tmp[j] = s
            tmp.pop()        
            cnt += 1
        ans = min(ans, cnt)
    print(ans)
if __name__ == "__main__":
    main()