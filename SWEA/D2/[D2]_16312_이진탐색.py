# 이진 탐색 함수 구현
# 비교할 때마다(함수를 호출할 때마다) count += 1
# 중앙값 == key 면 그 상태 카운트 반환
# 중앙값 < key 이면 중앙값 오른쪽을 잘라서 함수 호출
# 중앙값 > key 이면 중앙값 왼쪽을 잘라서 함수 호출
# 연속된 정수중에 찾는 문제: 없는 경우 없음 > 못 찾는 종료 조건 설정 불필요


def binary_search_count(left, right, key, count):
    c = (left + right) // 2
    count = count + 1
    if c == key:
        return count
    elif c < key:
        return binary_search_count(c, right, key, count)
    else:
        return binary_search_count(left, c, key, count)


T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    count = 0
    count_a = binary_search_count(1, P, Pa, 0)
    count_b = binary_search_count(1, P, Pb, 0)

    if count_a < count_b:
        print(f"#{tc} A")
    elif count_a > count_b:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")
