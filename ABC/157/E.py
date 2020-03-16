class SegTreeSum:
    def __init__(self, V):
        self.sz = len(V)
        N = 1
        while N < self.sz:
            N *= 2
        self.N = N
        self.node = [0] * (2 * self.N - 1)
        for i in range(self.sz):
            self.node[i + self.N - 1] = V[i]

        for i in range(self.N-2,-1,-1):
            self.node[i] = self.node[2*i+1] + self.node[2*i+2]

        
    def add(self,x,val):
        x += (self.N - 1)

        self.node[x] += val
        while x > 0:
            x = (x - 1) // 2
            self.node[x] = self.node[2*x+1] + self.node[2*x+2]

    def getsum(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.N
        
        if b <= l or a >= r:
            return 0
        
        if a <= l and b >= r:
            return self.node[k]

        vl = self.getsum(a,b, 2*k+1, l, (l+r)//2)
        vr = self.getsum(a,b, 2*k+2, (l+r)//2, r)
        return vl + vr

def main():
    N = int(input())
    S = input()
    Q = int(input())
    V = [0] * N
    seg_a = SegTreeSum(V)
    seg_b = SegTreeSum(V)
    seg_c = SegTreeSum(V)
    seg_d = SegTreeSum(V)
    seg_e = SegTreeSum(V)
    seg_f = SegTreeSum(V)
    seg_g = SegTreeSum(V)
    seg_h = SegTreeSum(V)
    seg_i = SegTreeSum(V)
    seg_j = SegTreeSum(V)
    seg_k = SegTreeSum(V)
    seg_l = SegTreeSum(V)
    seg_m = SegTreeSum(V)
    seg_n = SegTreeSum(V)
    seg_o = SegTreeSum(V)
    seg_p = SegTreeSum(V)
    seg_q = SegTreeSum(V)
    seg_r = SegTreeSum(V)
    seg_s = SegTreeSum(V)
    seg_t = SegTreeSum(V)
    seg_u = SegTreeSum(V)
    seg_v = SegTreeSum(V)
    seg_w = SegTreeSum(V)
    seg_x = SegTreeSum(V)
    seg_y = SegTreeSum(V)
    seg_z = SegTreeSum(V)
    Segs = [ seg_a, seg_b, seg_c, seg_d, seg_e, seg_f, \
        seg_g, seg_h, seg_i, seg_j, seg_k, seg_l, seg_m, \
        seg_n, seg_o, seg_p, seg_q, seg_r, seg_s, seg_t, \
        seg_u, seg_v, seg_w, seg_x, seg_y, seg_z ]
    for i in range(26):
        tmp = chr(i + 97)
        for j, k in enumerate(S):
            if k == tmp:
                Segs[i].add(j,1)
    
    for _ in range(Q):
        a, b, c = input().split()
        b = int(b) - 1
        if a == '1':
            d = ord(c) - 97
            Segs[i].add(b,1)
        else:
            ans = 0
            c = int(c)
            for i in range(26):
                if Segs[i].getsum(b,c):
                    ans += 1
            print(ans)





if __name__ == "__main__":
    main()