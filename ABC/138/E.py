from collections import defaultdict
from bisect import bisect_right

def main():
    S = input()
    T = input()
    d = defaultdict(list)
    for i, s in enumerate(S):
        d[s].append(i+1)
    pre = 0
    cnt = 0
    loop = 0
    len_S = len(S)
    for t in T:
        if not d[t]:
            print(-1)
            exit()
        index = bisect_right(d[t],pre)
        if index > len(d[t])-1:
            pre = 0
            loop += 1
            index = bisect_right(d[t],pre)
        pre = d[t][index]
        
    ans = loop * len_S + pre
    print(ans)






if __name__ == "__main__":
    main()