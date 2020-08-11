def main():
    s = input()
    S = set()
    A = list()
    pre = ''
    for i in range(len(s)):
        if s[i] in ['S','H','D','C']:
            if pre:
                S.add(pre)
                A.append(pre)
            pre = s[i]
        else:
            pre += s[i]
    S.add(pre)
    A.append(pre)
    spade = set(['S10','SJ','SQ','SK','SA'])
    diamond = set(['D10','DJ','DQ','DK','DA'])
    heart = set(['H10','HJ','HQ','HK','HA'])
    club = set(['C10','CJ','CQ','CK','CA'])
    ans = float('inf')
    cand = []
    if len(S & spade) == 5:
        tmp = 0
        for a in spade:
            tmp = max(tmp, A.index(a))
        if ans > tmp - 5:
            ans = tmp - 5
            cand.append('S')
            cand.append(tmp)

    if len(S & diamond) == 5:
        tmp = 0
        for a in diamond:
            tmp = max(tmp, A.index(a))
        if ans > tmp - 5:
            ans = tmp - 5
            cand.append('D')
            cand.append(tmp)

    if len(S & heart) == 5:
        tmp = 0
        for a in heart:
            tmp = max(tmp, A.index(a))
        if ans > tmp - 5:
            ans = tmp - 5
            cand.append('H')
            cand.append(tmp)

    if len(S & club) == 5:
        tmp = 0
        for a in club:
            tmp = max(tmp, A.index(a))
        if ans > tmp - 5:
            ans = tmp - 5
            cand.append('C')
            cand.append(tmp)
    if ans == -1:
        print(0)
        exit()
    
    ans = ''
    if cand[-2] == 'S':
        for i in range(cand[-1]):
            if not (A[i] in spade):
                ans += A[i]
        print(ans)
    elif cand[-2] == 'D':
        for i in range(cand[-1]):
            if not (A[i] in diamond):
                ans += A[i]
        print(ans)
    elif cand[-2] == 'H':
        for i in range(cand[-1]):
            if not (A[i] in heart):
                ans += A[i]
        print(ans)
    elif cand[-2] == 'C':
        for i in range(cand[-1]):
            if not (A[i] in club):
                ans += A[i]
        print(ans)

if __name__ == "__main__":
    main()