class Solve():
    N, A, B = map(int, input().split())
    H = [0] * N
    for i in range(N):
        H[i] = int(input())

    def isOK(self,x):
        cnt = 0
        for i in range(self.N):
            now = self.H[i] - self.B * x
            if now > 0:
                cnt += now // (self.A - self.B) if now % (self.A - self.B) == 0 else (now // (self.A - self.B)) + 1
            if cnt > x:
                return False
        return True
    
    def binary_search(self):
        ng = -1
        ok = 1010101010
        while (abs(ok - ng)) > 1:
            mid = (ok + ng) // 2
            if self.isOK(mid):
                ok = mid
            else:
                ng = mid

        return ok

if __name__ == "__main__":
    ans = Solve().binary_search()
    print(ans)