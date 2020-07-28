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
        #tmp = max(dist)
        #cand = []
        #for i in range(N):
        #    if tmp == dist[i]:
        #        cand.append(i)
        score = float('inf')
        axios = []
        for c in range(N):
            tmp_x = 0
            tmp_y = 0
            # x軸に引く場合
            for j in range(N):
                tmp_x += min(dist[j], P[j]*abs(X[c]-X[j]))
            if score > tmp_x:
                if axios:
                    axios.pop(-1)
                axios.append([X[c],'x'])
                score = tmp_x
            # y軸に引く場合
            for j in range(N):
                tmp_y += min(dist[j], P[j]*abs(Y[c]-Y[j]))
            if score > tmp_y:
                if axios:
                    axios.pop(-1)
                axios.append([Y[c],'y'])
                score = tmp_y
        print(axios)
        if axios[0][1] == 'x':
            for j in range(N):
                dist[j] = min(dist[j], P[j]*abs(axios[0][0]-X[j]))
        else:
            for j in range(N):
                dist[j] = min(dist[j], P[j]*abs(axios[0][0]-Y[j]))
        print(dist)
        print(sum(dist))

    

if __name__ == "__main__":
    main()