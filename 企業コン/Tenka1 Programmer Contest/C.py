
def main():
    N = int(input())
    for h in range(1,3501):
        for n in range(1,3501):
            if 4 * h * n - N * n - N * h == 0:
                continue
            w = (N * h * n) / (4 * h * n - N * n - N * h)
            if w > 0 and w.is_integer():
                print(h,n,int(w))
                exit()




if __name__ == "__main__":
    main()