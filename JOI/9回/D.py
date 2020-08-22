from itertools import permutations

def main():
    n = int(input())
    k = int(input())
    card = [input() for _ in range(n)]
    ans = set()
    for i in range(2**n):
        cand = []
        for j in range(n):
            if (i >> j) & 1:
                cand.append(card[j])
        if len(cand) != k:
            continue
        for pattern in permutations(cand):
            a = ''.join(pattern)
            ans.add(a)

    print(len(ans))
        

if __name__ == "__main__":
    main()