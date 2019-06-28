# とりあえずUnion-Findを実装してみる
class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納する。par[x] == [x]の時、そのノードは根
        self.par = [i for i in range(n)]
        # 木の高さを格納する (初期状態では0)
        # self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] == x:
            return x
        # 根でないなら、親の要素で再検索
        else:
            # 探索していく過程で親を書き換える
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    # 併合
    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)
        return x == y
        # 木の高さを比較し、低いほうから高いほうに辺を張る
        # if self.rank[x] < self.rank(y):
        #    self.par[x] = y
        # else:
        #    self.par[y] = x
        # 木の高さが一緒だったら片方増やす
        #    if self.rank[x] == self.rank[y]:
        #        self.rank[x] += 1

N, K, L = map(int, input().split())
uf1 = UnionFind(N)
uf2 = UnionFind(N)

for k in range(K):
    p, q = map(int, input().split())
    uf1.union(p-1, q-1)

for l in range(L):
    r, s = map(int, input().split())
    uf2.union(r-1, s-1)
ans = {}
key_list = []
for i in range(N):
    root1 = uf1.find(i)
    root2 = uf2.find(i)
    print(root1,root2)

    key = str(root1) + "_" + str(root2)
    key_list.append(key)

    if key in ans.keys():
        ans[key] += 1
    else:
        ans[key] = 1

for i in range(N):
    print(ans[key_list[i]], end=' ')