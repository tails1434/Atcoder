def main():
    N = int(input())
    boxes = []
    for _ in range(N):
        h, w = map(int, input().split())
        boxes.append([h,w])
    ans = 0
    sorted_boxes = sorted(boxes, key=lambda x:(x[0], x[1]), reverse=True)
    cnt = 1
    now_h = sorted_boxes[0][0]
    now_w = sorted_boxes[0][1]
    for i in range(1,N):
        if now_h > sorted_boxes[i][0] and now_w > sorted_boxes[i][1]:
            now_h = sorted_boxes[i][0]
            now_w = sorted_boxes[i][1]
            cnt += 1
    ans = max(ans,cnt)
    sorted_boxes = sorted(boxes, key=lambda x:(x[1], x[0]), reverse=True)
    cnt = 1
    now_h = sorted_boxes[0][0]
    now_w = sorted_boxes[0][1]
    for i in range(1,N):
        if now_h > sorted_boxes[i][0] and now_w > sorted_boxes[i][1]:
            now_h = sorted_boxes[i][0]
            now_w = sorted_boxes[i][1]
            cnt += 1
    ans = max(ans,cnt)
    print(ans)
    
if __name__ == "__main__":
    main()