def main():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())
    dis1_a = A1 * T1
    dis1_b = B1 * T1
    dis2_a = A2 * T2
    dis2_b = B2 * T2

    if dis1_a + dis2_a == dis1_b + dis2_b:
        print('infinity')
        exit()

    if (dis1_a - dis1_b) > 0 and (dis2_a + dis1_a - dis2_b - dis1_b) > 0:
        print(0)
        exit()

    if (dis1_a - dis1_b) < 0 and (dis2_a + dis1_a - dis2_b - dis1_b) < 0:
        print(0)
        exit()

    #print(dis1_a - dis1_b)
    #print(dis2_a + dis1_a - dis2_b - dis1_b)
    #print(dis2_a + dis1_a - dis2_b - dis1_b + (dis1_a - dis1_b))
    #print(2*(dis2_a + dis1_a - dis2_b - dis1_b))

    diff = (dis1_a - dis1_b) - (dis2_a + dis1_a - dis2_b - dis1_b + (dis1_a - dis1_b))
    cnt = (dis1_a - dis1_b) // diff
    print(cnt * 2 if (dis1_a - dis1_b) % diff == 0 else cnt * 2 + 1)

    


if __name__ == "__main__":
    main()