# 덤프 수 만큼
# 박스 최댓값 -1, 최솟값 +1
# 덤프 끝난 후 다시 최대/최소 탐색

for t in range(10):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):
        max_box, max_idx = boxes[0], 0
        min_box, min_idx = boxes[0], 0

        for i in range(len(boxes)):
            if max_box < boxes[i]:
                max_box = boxes[i]
                max_idx = i
            if min_box > boxes[i]:
                min_box = boxes[i]
                min_idx = i

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    final_max = final_min = boxes[0]
    for i in range(len(boxes)):
        if final_max < boxes[i]:
            final_max = boxes[i]
        if final_min > boxes[i]:
            final_min = boxes[i]

    print(f'#{t + 1} {final_max - final_min}')
