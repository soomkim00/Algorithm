import sys

sys.stdin = open("input.txt", "r")

# 양 쪽을 번갈아가면서 보다가 찾은 숫자

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        arr = list(map(int, input().split()))
        num = list(map(int, input().split()))

        result = 0  # 만족하는 정수의 개수
        for n in num:
            # 양 끝 값으로 왼쪽, 오른쪽 설정
            l = 0
            r = N - 1
            find_check = False  # 찾았는지?
            dir_li = []  # 탐색한 방향들을 순서대로 모은 리스트

            while l <= r:  # 왼쪽과 오른쪽이 역전되지 않는 동안
                m = (l + r) // 2  # 중앙 값 재계산
                if arr[m] == n:  # 찾았다
                    find_check = True  # 찾음 체크
                    break
                elif arr[m] > n:  # 목표 값보다 중앙이 크다 -> 목표 값은 왼쪽에 있다
                    r = m - 1
                    dir_li.append(1)
                else:  # 반대의 경우는 목표 값이 오른쪽
                    l = m + 1
                    dir_li.append(-1)
            # 찾았으면, 방향 검사
            if find_check:
                # 같은 방향 두 번 나왔는지를 체크
                for i in range(len(dir_li) - 1):
                    if abs(dir_li[i] + dir_li[i + 1]) >= 2:
                        break
                else:
                    result += 1

        print(f"#{tc} {result}")
