import sys

sys.stdin = open("input.txt", "r")


# 중간 요소를 피벗으로 설정
def partition(l, r):
    m = (l + r) // 2  # 중간 인덱스
    pivot = arr[m]  # 피벗은 중간 "값"
    arr[l], arr[m] = arr[m], arr[l]  # 피벗을 왼쪽으로 옮기기
    i = l + 1
    j = r

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j


def quick_sort(l, r):
    # 범위가 있는 동안, 즉 l와 r가 뒤집히지 않는 동안
    if l < r:
        pivot = partition(l, r)  # 피벗 하나 위치를 잡고
        quick_sort(l, pivot - 1)  # 왼쪽범위 다시 정렬
        quick_sort(pivot + 1, r)  # 오른쪽범위 다시 정렬


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))

        quick_sort(0, len(arr) - 1)

        print(f"#{tc} {arr[N // 2]}")
