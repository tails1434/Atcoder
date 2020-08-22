from collections import deque

def main():
    A = [list(input()) for _ in range(10)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    cnt = 0
    for h in range(10):
        for w in range(10):
            if A[h][w] == 'x':
                visited = [[False] * 10 for _ in range(10)]
                Q = deque([[h,w]])
                while Q:
                    y, x = Q.pop()
                    visited[y][x] = True
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < 10 and 0 <= ny < 10:
                            if A[ny][nx] == 'o' and (not visited[ny][nx]):
                                Q.append([ny,nx])
                flag = True
                for a in range(10):
                    for b in range(10):
                        if A[a][b] == 'o' and (not visited[a][b]):
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print('YES')
                    exit()

    print('NO')


if __name__ == "__main__":
    main()