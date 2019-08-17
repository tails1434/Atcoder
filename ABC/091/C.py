from operator import itemgetter

def main():
    N = int(input())
    
    red = [[int(i) for i in input().split()] for i in range(N)]
    blue = [[int(i) for i in input().split()] for i in range(N)]

    # 青よりx,y座標のが小さい赤の中で、最もyが大きいものから削除するため
    # 青はxでソート、赤はyで大きい順でソートする
    sort_red = sorted(red, key=itemgetter(1), reverse=True)
    sort_blue = sorted(blue, key=itemgetter(0))

    cnt = 0
    for b in sort_blue:
        for r in sort_red:
            if r[0] < b[0] and r[1] < b[1]:
                cnt += 1
                sort_red.remove(r)
                break
    print(cnt)


main()