from collections import deque

def main():
    Q, L = map(int, input().split())
    d = deque([])
    cnt = 0
    for _ in range(Q):
        query = input().split()
        if query[0] == 'Size':
            print(cnt)
        elif query[0] == 'Push':
            N = int(query[1])
            M = int(query[2])
            if cnt + N > L:
                print('FULL')
                exit()
            d.append([M,N])
            cnt += N
        elif query[0] == 'Pop':
            N = int(query[1])
            if cnt - N < 0:
                print('EMPTY')
                exit()
            cnt -= N
            while N > 0:
                m, n = d.pop()
                if n > N:
                    n -= N
                    d.append([m,n])
                    N = 0
                elif n < N:
                    N -= n
                elif n == N:
                    N = 0
        elif query[0] == 'Top':
            if cnt == 0:
                print('EMPTY')
                exit()
            m, n = d.pop()
            print(m)
            d.append([m,n])

    print('SAFE')

if __name__ == "__main__":
    main()