import sys

sys.stdin = open("input.txt", "r")


# 각 자석의 (위, 왼쪽, 오른쪽)을 가리키는 포인터를 설정, 초기값은 (0, 6, 2)
# 자석이 시계방향으로 돌아간다 -> 포인터를 반시계방향으로 돌린다 (포인터를 -1 뺀다)
# 매 번 명령어를 실행할 때마다
# 1. 첫 위치 pos에서 왼쪽, 오른쪽으로 증가시키면서 마주보는 자성을 비교해서 어느 자석들을 회전시킬지 rotate_li에 저장 (회전 방향 바꿔가면서)
#   - ex 왼쪽 자석의 오른쪽 포인터의 자성 값 != 그 전 자석의 왼쪽 포인터의 자성 값 : (왼쪽 자석 위치, 그 전 자석 방향 * -1) 저장
# 2. 리스트 안의 자석들을 방향에 맞게 회전
#   - 시계방향이면 세 포인터를 -1, 0이면 7로 변환, 반시계는 +1
# 3. 최종 자성들의 위 포인터들의 자성을 검사하면서 점수 채점

# 회전 회오리-!
def rotate(m, d):
    # print(m, d)
    if d == 1:
        for i in range(3):
            point[m][i] = point[m][i] - 1 if point[m][i] >= 1 else 7
    elif d == -1:
        for i in range(3):
            point[m][i] = (point[m][i] + 1) % 8


# 점수 계산
def cal_score():
    result = 0
    s_li = [1, 2, 4, 8]
    for i in range(4):
        if magnet[i][point[i][0]]:
            result += s_li[i]
    return result


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        K = int(input())
        magnet = [list(map(int, input().split())) for _ in range(4)]
        commands = [list(map(int, input().split())) for _ in range(K)]

        # 각 톱니바퀴의 위, 왼쪽, 오른쪽 좌표 0 1 2
        point = [[0, 6, 2] for _ in range(4)]

        # 회전 실시
        for pos, dir in commands:
            rotate_li = []  # (돌릴 위치, 돌릴 방향) 리스트
            pos -= 1  # 입력값은 1~4 -> 인덱스로 변환
            rotate_li.append((pos, dir))  # 시작 위치 추가

            # 어디까지 돌릴것인가
            # 왼쪽 검사
            temp = dir
            for i in range(1, 4):
                left = pos - i
                if left < 0:  # 범위 체크
                    break
                if magnet[left][point[left][2]] == magnet[left + 1][point[left + 1][1]]:
                    break
                else:
                    temp = - temp  # 회전 방향 반전
                    rotate_li.append((left, temp))
            # 오른쪽 검사
            temp = dir
            for i in range(1, 4):
                right = pos + i
                if right >= 4:
                    break
                if magnet[right - 1][point[right - 1][2]] == magnet[right][point[right][1]]:
                    break
                else:
                    temp = - temp
                    rotate_li.append((right, temp))

            # 자석 회전
            for p, d in rotate_li:
                rotate(p, d)

        # 점수 계산
        score = cal_score()

        print(f"#{tc} {score}")

"""
#1 10
#2 14
#3 3
#4 13
#5 15
#6 10
#7 2
#8 6
#9 5
#10 4
"""
