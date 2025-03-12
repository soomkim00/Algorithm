# N개의 숫자 중 2개의 위치를 c 번 교환한다
# 1. 0 ~ N-1 중 2 개의 위치를 고른다
# 1-1 교환을 위해선 서로 다른 위치를 골라야 하므로 순열
# 1-2 서로 다른 위치들을 list로 만들어 놓는다 ((0,1), (0,2), (1,0), (1,2), ...)
# 2. c 번의 교환을 고른다 == 위치 list들 중 c 개를 고른다
# 2-1 교환은 동일한 위치에서 여러번 발생이 가능하다, 즉 중복순열
# 2-2 ex (0,1) (0,1), (0,1) == 0번째 숫자와 1번째 숫자를 세번 교환한다.
# 3. 최종 교환이 끝난 숫자들을 변환 후 최대값을 구한다.

import sys

sys.stdin = open("input.txt", "r")

# 1. 서로 교환할 위치쌍의 모음 (순열)
pos = []  # 서로 교환할 위치 2개를 담을 list
positions = []  # pos 들을 담을 list


def select_pos(cnt, n):
    # 기저 조건 : 교환할 위치는 2개를 골라야 하므로, 2개가 되면 종료
    if cnt == 2:
        positions.append(tuple(pos))  # list로 저장하게되면 pos에 대한 참조값만 저장이 된다..!
        return

    # 0~n-1 까지 위치(바꿀 숫자의)중 두 가지를 고르는 순열 생성
    for idx in range(n):
        # 해당 위치를 이미 골랐으면 넘어가기
        if used[idx]:
            continue

        used[idx] = 1
        pos.append(idx)
        select_pos(cnt + 1, n)
        pos.pop()
        used[idx] = 0


# 위치의 순서쌍을 c 번 골라서 교환하자
def exchange_score(cnt, c):
    # 기저조건: c번 교환이 일어나면 점수 저장
    if cnt == c:
        result.add(''.join(copy))

T = int(input())

for tc in range(1, T + 1):
    board, chance = input().split()
    board = list(map(int, board))
    chance = int(chance)
    N = len(board)  # 숫자의 개수
    used = [0] * N  # 숫자 사용 여부 체크 (바꿀 위치는 서로 다른 위치여야 하기 때문에!)
    result = set()

    select_pos(0, N)
    exchange_score(0, chance)
    print(f"#{tc} ")
