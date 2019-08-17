from collections import defaultdict
from itertools import combinations

def main():
    N = int(input())

    S = defaultdict(int)

    for i in range(N):
        tmp = input()
        if tmp[0] == "M":
            S["M"] += 1
        elif tmp[0] == "A":
            S["A"] += 1
        elif tmp[0] == "R":
            S["R"] += 1
        elif tmp[0] == "C":
            S["C"] += 1
        elif tmp[0] == "H":
            S["H"] += 1

    ans = 0

    # 文字を3種類ピックアップする組み合わせごとに数を求めて
    # 足し合わせる
    for a, b, c in combinations(S.values(), 3):
        ans += a * b * c

    print(ans)
main()