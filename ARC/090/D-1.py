class UnionFind():
    def __init__(self, main):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
    def same(self, x, y):
        return self.find(x) == self.find(y)

    


def main():
    N, M = map(int, input().split())
    uni = UnionFind(N)
    dist = [[0] * N for _ in range(N)]
    for _ in range(M):
        L, R, D = map(int, input().split())
        L -= 1
        R -= 1
        dist[L][R] = D
        if uni.same(L, R):


if __name__ == "__main__":
    main()