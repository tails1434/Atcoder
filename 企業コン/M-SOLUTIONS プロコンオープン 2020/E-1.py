from collections import defaultdict

def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    P = [0] * N
    dist = [0] * N
    x = defaultdict(int)
    y = defaultdict(int)
    for i in range(N):
        X[i], Y[i], P[i] = map(int, input().split())
        dist[i] = P[i] * min(abs(X[i]), abs(Y[i]))
        x[X[i]] += P[i] * X[i]
        y[Y[i]] += P[i] * Y[i]

    print(sum(dist))
    for K in range(1,N+1):
        score = sum(dist)
        
        while K > 0:
            cand_x = []
            cand_y = []
            axios = []
            mx = 0
            for i, j in x.items():
                mx = max(j,mx)
            
            my = 0
            for i, j in y.items():
                my = max(j,my)
            if mx > my:
                for i, j in x.items():
                    if mx == j:
                        cand_x.append(x[i])
            elif mx < my:
                for i, j in y.items():
                    if my == j:
                        cand_y.append(y[i])
            else:
                for i, j in x.items():
                    if mx == j:
                        cand_x.append(x[i])
                for i, j in y.items():
                    if my == j:
                        cand_y.append(y[i])
            print(cand_x,cand_y)
            for c in cand_x:
                tmp_x = 0
                # x軸に引く場合
                for j in range(N):
                    tmp_x += min(dist[j], P[j]*abs(c-X[j]))
                if score > tmp_x:
                    if axios:
                        axios.pop(-1)
                    axios.append([c,'x'])
                    score = tmp_x
            for c in cand_y:
                tmp_y = 0
                # y軸に引く場合
                for j in range(N):
                    tmp_y += min(dist[j], P[j]*abs(c-Y[j]))
                if score > tmp_y:
                    if axios:
                        axios.pop(-1)
                    axios.append([c,'y'])
                    score = tmp_y
            print(axios)
            if axios[0][1] == 'x':
                for j in range(N):
                    dist[j] = min(dist[j], P[j]*abs(axios[0][0]-X[j]))
                x[c] = 0
            else:
                for j in range(N):
                    dist[j] = min(dist[j], P[j]*abs(axios[0][0]-Y[j]))
                y[c] = 0
            
            K -= 1
        print(sum(dist))

if __name__ == "__main__":
    main()