from collections import Counter
from itertools import permutations

def main():
    S = list(input())
    N = len(S)
    C = Counter(S)
    even = 0
    odd = 0
    for c in C.values():
        if c % 2 == 0:
            even += 1
        else:
            odd += 1
    
    if odd == 0:
        print(len(S))
        exit()
    
    ans = 2 * ((N-odd)//(2*odd)) + 1

    print(ans)


if __name__ == "__main__":
    main()