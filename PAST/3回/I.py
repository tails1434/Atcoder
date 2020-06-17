import numpy as np
import pandas as pd

def main():
    N = int(input())
    Q = int(input())
    A = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            A[i][j] = N * i + j
    arr_t = np.array(A)

    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            i = q[1]-1
            j = q[2]-1
            arr_t[i], arr_t[j] = arr_t[j], arr_t[i]
        elif q[0] == 2:
            i = q[1]-1
            j = q[2]-1
        elif q[0] == 3:
            arr_t = arr_t.T
        else:
            i = q[1]-1
            j = q[2]-1
            print(arr_t[i][j])



if __name__ == "__main__":
    main()