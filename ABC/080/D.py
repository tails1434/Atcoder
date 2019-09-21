from collections import defaultdict
from itertools import accumulate

def main():
    N, C = map(int, input().split())
    programs = defaultdict(list)

    for _ in range(N):
        s,t,c = map(int, input().split())
        programs[c].append((s,t))

    imos = [0] * (10**5 + 1)
    for c, p in programs.items():
        p.sort()
        # チャンネルごとに連結処理を行う
        ps, pt = p[0]
        for s, t in p[1:]:
            if pt == s:
                pt = t
            else:
                imos[ps - 1] += 1
                imos[pt] -= 1
                ps, pt = s, t

        imos[ps - 1] += 1
        imos[pt] -= 1

    print(max(accumulate(imos)))

main()