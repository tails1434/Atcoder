from bisect import bisect_left

def main():
    N = int(input())

    ball = []
    for i in range(N):
        a, b = map(int, input().split())
        ball.append([a,b,'r'])
    for i in range(N):
        c, d = map(int, input().split())
        ball.append([c,d,'b'])

    sort_ball = sorted(ball, key=lambda x:(-x[0],x[1]))
    ans = 0
    cand = []
    for i in range(2*N):
        if sort_ball[i][2] == 'b':
            cand.append(sort_ball[i][1])
        if sort_ball[i][2] == 'r':
            if not cand:
                continue
            cand.sort()
            b_y = bisect_left(cand, sort_ball[i][1])
            if b_y == len(cand):
                continue
            ans += 1
            cand.pop(b_y)

    print(ans)

        

    
    
    

if __name__ == "__main__":
    main()