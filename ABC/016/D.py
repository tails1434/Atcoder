def check_cross(Ax,Ay,Bx,By,Cx,Cy,Dx,Dy):
    ta = (Cx - Dx) * (Ay - Cy) + (Cy - Dy) * (Cx - Ax)
    tb = (Cx - Dx) * (By - Cy) + (Cy - Dy) * (Cx - Bx)
    tc = (Ax - Bx) * (Cy - Ay) + (Ay - By) * (Ax - Cx)
    td = (Ax - Bx) * (Dy - Ay) + (Ay - By) * (Ax - Dx)

    return tc * td < 0 and ta * tb < 0

def main():
    Ax, Ay, Bx, By = map(int, input().split())
    N = int(input())
    X = [0] * N
    Y = [0] * N
    cnt = 0
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    X += [X[0]]
    Y += [Y[0]]

    for i in range(N):
        if check_cross(Ax,Ay,Bx,By,X[i],Y[i],X[i+1],Y[i+1]):
            cnt += 1
    ans = 1 + cnt // 2
    print(ans)


if __name__ == "__main__":
    main()