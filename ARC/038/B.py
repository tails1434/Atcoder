def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    memo = [[None] * W for _ in range(H)]
    def grundy(h,w):
        if h >= H or w >= W or S[h][w] == '#':
            return True
        if memo[h][w] != None:
            return memo[h][w]
        
        result = False
        if not grundy(h+1,w):
            result = True
        if not grundy(h,w+1):
            result = True
        if not grundy(h+1,w+1):
            result = True

        memo[h][w] = result
        return memo[h][w]

    if grundy(0,0):
        print('First')
    else:
        print('Second')
    

if __name__ == "__main__":
    main()