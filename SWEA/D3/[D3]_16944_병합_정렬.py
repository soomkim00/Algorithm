import sys

sys.stdin = open("input.txt", "r")


# 원소가 하나 남을 때 까지 분할
def merge_sort(li: list):
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    left_li = merge_sort(left)
    right_li = merge_sort(right)

    merge_list = merge(left_li, right_li)
    return merge_list


# 병합
def merge(left: list, right: list):
    global cnt
    # 끝 원소 비교해서 카운트 증가
    if left[-1] > right[-1]:
        cnt += 1

    result = [0] * (len(left) + len(right))
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 남은 원소
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 오른쪽 남은 원소
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))

        cnt = 0
        sorted_arr = merge_sort(arr)

        print(f"#{tc} {sorted_arr[N // 2]} {cnt}")

"""
#1 2 0
#2 6 6
"""
