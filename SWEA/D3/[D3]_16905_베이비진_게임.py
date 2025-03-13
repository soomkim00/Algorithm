import sys

sys.stdin = open("input.txt", "r")

# 3장은 있어야 판단이 가능하니까. 서로 세 장을 나눈 시점부터
# 플레이어 1 과 플레이어 2의 baby-gin 여부를 각각 검사
# 카드를 가져갈때마다 검사
# 끝까지 검사 결과 True가 없었으면 0 출력


def is_baby_gin(li: list):
    # triplet 검사. 정렬한 후 순서대로 보면서 세 번 같은 원소가 나오는가?
    li.sort()
    for i in range(len(li)-2):
        if li[i] == li[i+1] == li[i+2]:
            return True

    # run 검사를 위해서 중복값 제거 후 세 번 1씩 증가하는 값이 나오는가?
    # 2 3 3 4 같은 경우를 검사하기 위해서 중복 제거!
    li = list(set(li))
    for i in range(len(li)-2):
        if li[i+1] - li[i] == 1 and li[i+2] - li[i+1] == 1:  # run?
            return True
    return False


T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    A, B = [], []
    for i in range(0, 12, 2):
        A.append(arr[i])
        B.append(arr[i + 1])
        if i >= 5:
            if is_baby_gin(A):
                print(f"#{tc} 1")
                break
            if is_baby_gin(B):
                print(f"#{tc} 2")
                break
    else:
        print(f"#{tc} 0")
