from collections import deque

def func(x):
    return x - 1

def main():
    N = int(input())
    A = [deque(map(func,map(int, input().split()))) for _ in range(N)]
    # 前日試合した人
    pre_players = range(N)
    game_cnt = 0
    day_cnt = 0
    max_cnt = N * (N - 1) // 2
    while day_cnt < max_cnt:
        # 当日試合した人
        players = set()
        for p in pre_players:
            if p in players:
                continue
            if not A[p]:
                continue
            opp = A[p][0]
            if opp in players:
                continue

            if p == A[opp][0]:
                A[p].popleft()
                A[opp].popleft()
                players |= {p,opp}
                game_cnt += 1

        pre_players = players
        day_cnt += 1

        if max_cnt == game_cnt:
            break

    if game_cnt != max_cnt:
        print(-1)
    else:
        print(day_cnt)
    
    

if __name__ == "__main__":
    main()