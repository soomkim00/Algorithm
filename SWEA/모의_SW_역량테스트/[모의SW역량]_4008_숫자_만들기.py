import sys

sys.stdin = open("input.txt", "r")


# 연산자를 리스트로 저장해놓고
# 순열 생성해서 계산


def recur(cnt):
    if cnt == N - 1:
        cal(path)
        return

    for num in range(N - 1):
        if used[num]:
            continue

        # 같은 레벨에서 앞에 사용하지 않은 중복 연산자 건너뛰기
        if num and oper_li[num] == oper_li[num - 1] and not used[num - 1]:
            continue

        used[num] = 1
        path.append(oper_li[num])
        recur(cnt + 1)
        path.pop()
        used[num] = 0


def cal(li: list):
    global max_v, min_v
    result = numbers[0]
    for i in range(N - 1):
        if li[i] == 0:
            result += numbers[i + 1]
        elif li[i] == 1:
            result -= numbers[i + 1]
        elif li[i] == 2:
            result *= numbers[i + 1]
        elif li[i] == 3:
            result /= numbers[i + 1]
            result = int(result)
    max_v = max(result, max_v)
    min_v = min(result, min_v)


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        oper = list(map(int, input().split()))
        numbers = list(map(int, input().split()))

        oper_li = []

        # 연산자를 각 개수대로 풀어서 리스트에 저장하자
        for i in range(4):
            for _ in range(oper[i]):
                oper_li.append(i)

        # 조건에 의한 최대, 최소값 설정
        min_v, max_v = 100000001, -100000001

        # 0~N-1 개의 순열 생성
        path = []
        used = [0] * (N - 1)
        recur(0)
        print(f"#{tc} {max_v - min_v}")

"""
#1 24
#2 8
#3 144
#4 8
#5 91
#6 150
#7 198
#8 2160
#9 46652
#10 701696
"""
