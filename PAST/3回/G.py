from collections import deque

def main():
    N, X, Y = map(int, input().split())
    X += 201
    Y += 201
    d = [[float('inf')] * 405 for _ in range(405)]
    obstacle = [[True] * 405 for _ in range(405)]
    for _ in range(N):
        x, y = map(int, input().split())
        x += 201
        y += 201
        obstacle[x][y] = False

    Q = deque([[201,201]])
    dt = [(1,1),(0,1),(-1,1),(1,0),(-1,0),(0,-1)]
    d[201][201] = 0
    while Q:
        x, y = Q.popleft()

        if x == X and y == Y:
            break

        for dx, dy in dt:
            nx = x + dx
            ny = y + dy

            if 0 <= nx <= 402 and 0 <= ny <= 402:
                if obstacle[nx][ny]:
                    if d[nx][ny] == float('inf'):
                        d[nx][ny] = d[x][y] + 1
                        Q.append([nx,ny])

    if d[X][Y] == float('inf'):
        print(-1)
    else:
        print(d[X][Y])    

        




if __name__ == "__main__":
    main()