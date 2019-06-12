N,M = map(int,input().split())

# kの値は特に必要ないので最初から取得しない
S=[list(map(int,input().split()))[1:] for i in range(M)]
p = list(map(int,input().split()))
ans = 0
for i in range(1<<N): #スイッチのオンオフ状態
    
    for m in range(M):  #電球の状態 
        count = 0
        for s in S[m]:
            if i & (1<<(s-1)) != 0:
                count += 1
                # 電球に対するスイッチのonの数を取得する
        if count%2 != p[m]:
            break
    else:
        # あるスイッチのパターンに対して各電球がOKだったらカウントする
        ans +=1
print(ans)