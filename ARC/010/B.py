from datetime import *

def main():
    N = int(input())
    dates = []
    d = date(2012,1,1)
    while d != date(2013,1,1):
        dates.append(d)
        d += timedelta(days=1)
    
    happy = []
    for _ in range(N):
        m, d = map(int, input().split('/'))
        happy.append(date(2012,m,d))
    
    is_holiday = [0] * (len(dates) + 1)
    for i, d in enumerate(dates):
        if d.weekday() in [5,6]:
            is_holiday[i] += 1
        
        if d in happy:
            is_holiday[i] += 1

        if is_holiday[i] >= 2:
            is_holiday[i+1] = is_holiday[i] - 1
            is_holiday[i] = 1 

    ans = 0
    cnt = 0
    for x in is_holiday[:-1]:
        if x == 0:
            cnt = 0
            continue
        cnt += 1
        ans = max(ans, cnt)

    print(ans)

if __name__ == "__main__":
    main()