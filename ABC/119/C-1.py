from itertools import product

def main():
    N, A, B, C = map(int, input().split())
    L = list(int(input()) for _ in range(N))
    # A => 0
    # B => 1
    # C => 2
    ans = float('inf')
    for item in product(range(4), repeat=N):
        length_A = 0
        cnt_A = 0
        score_A = 0
        length_B = 0
        cnt_B = 0
        score_B = 0
        length_C = 0
        cnt_C = 0
        score_C = 0
        for i,j in enumerate(item):
            if j == 0:
                length_A += L[i]
                cnt_A += 1
            if j == 1:
                length_B += L[i]
                cnt_B += 1
            if j == 2:
                length_C += L[i]
                cnt_C += 1
        if cnt_A == 0 or cnt_B == 0 or cnt_C == 0:
            continue
        score_A += abs(A - length_A) + 10 * (cnt_A - 1)
        score_B += abs(B - length_B) + 10 * (cnt_B - 1)
        score_C += abs(C - length_C) + 10 * (cnt_C - 1)
        ans = min(ans, score_A + score_B + score_C)
    print(ans)

if __name__ == "__main__":
    main()