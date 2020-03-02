from math import hypot

def half_point(p1,p2):
    x = (p1[0] + p2[0]) / 2
    y = (p1[1] + p2[1]) / 2
    r = hypot(p1[0] - p2[0], p1[1] - p2[1]) / 2
    return (x, y, r)

def three_points_on_a_line(p1,p2,p3):
    dx1 = p1[0] - p2[0]
    dy1 = p1[1] - p2[1]
    dx2 = p1[0] - p3[0]
    dy2 = p1[1] - p3[1]

    return dx1 * dy2 == dx2 * dy1

def same_point(p1,p2,p3):
    return p1 == p2 or p1 == p3 or p2 == p3

def gaisin(p1,p2,p3):
    a = p1[0]
    b = p1[1]
    c = p2[0]
    d = p2[1]
    e = p3[0]
    f = p3[1]

    aa = a * a
    bb = b * b
    cc = c * c
    dd = d * d
    ee = e * e
    ff = f * f

    py = ((e - a) * (aa + bb - cc - dd) - (c - a) * (aa + bb - ee- ff)) / (2 * (e - a)*(b - d) - 2 * (c - a) * (b - f))

    px = (2 * (b - f) * py - aa - bb + ee + ff) / (2 * (e - a)) \
        if (c == a) else (2 * (b - d) * py - aa - bb + cc + dd) / (2 * (c - a))

    r = hypot(px - a, py - b)

    return (px,py,r)

def in_c(x,y,r,px,py):

    if hypot(x-px,y-py) > r+10**(-6):
        return False
 
    return True

def main():
    
    N = int(input())
    X = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append((x,y))
    
    cand = []
    for i in range(N):
        for j in range(i+1,N):
            # 直線の中点を候補に追加する
            cand.append(half_point(X[i],X[j]))

            # 三点から外心を求める
            for k in range(j+1,N):
                if same_point(X[i],X[j],X[k]) or three_points_on_a_line(X[i],X[j],X[k]):
                    continue
                cand.append(gaisin(X[i],X[j],X[k]))

    ans = float('inf')
    for px, py, r in cand:
        flag = True
        for x, y in X:
            if not in_c(x,y,r,px,py):
                flag = False
                break 
        if flag:
            ans = min(ans, r)

    print(ans)



if __name__ == "__main__":
    main()