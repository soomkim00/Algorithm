# 벽돌 떨어뜨릴 열의 순서쌍을 dfs로 만들고(중복순열)
# 각 순서쌍으로 벽돌 부수기 + 위치 조정하기를 수행 후
# 남아있는 벽돌 수를 세서 result에 넣고, 최종 result 최소값 출력
# 만약 result에 0이 들어갔으면 이미 최소값이므로 종료
# 종료 조건에서 재귀가 return이 발생해 시간 최적화가 더이상은 무리.. 함수화가 무조건 좋은건 아니다..!

from collections import deque
import copy

# import sys
#
# sys.stdin = open("input.txt", "r")


def select_pos(n: int, w: int, h: int, p_li: list):
    # 결과 최소값이 0이면. 더 이상 구할 필요 없으므로 return
    # (벽돌을 다 깬 경우)
    if result and min(result) == 0:
        return

    # 공을 n번 떨어뜨릴 위치를 다 정했으면
    if len(p_li) == n:
        drop_ball(w, h, p_li)
        return

    for i in range(w):  # 0 부터 w-1 까지의 숫자로 조합 생성
        p_li.append(i)  # 하나의 원소를 추가하고
        select_pos(n, w, h, p_li)  # 재귀 호출
        p_li.pop()  # 넣은 원소 제거 (백트래킹)


def drop_ball(w: int, h: int, pos_li: list):
    # 원본 벽돌 상태 복사해놓고
    t_bricks = copy.deepcopy(bricks)  # 이중 리스트이기때문에 깊은 복사

    # p_li에 따라서 break_bricks()를 호출
    # 이후 adj_bricks()를 호출해서 벽돌 위치 조정
    for pos in pos_li:
        break_bricks(pos, w, h, t_bricks)
        adj_bricks(w, h, t_bricks)

    # p_li 전부 탐색 후 합계를 구해서 result에 추가
    cnt = 0
    for r in range(h):
        for c in range(w):
            if t_bricks[r][c]:
                cnt += 1
    result.append(cnt)


def break_bricks(p: int, w: int, h: int, t_br: list):
    # p 위치의 가장 높은 블럭을 선택한 후
    r = 0
    c = p
    for i in range(h):
        r = i
        if t_br[r][c]:
            break
    # bfs로 탐색
    # 델타로 K-1 범위만큼 탐색해서 숫자면 큐에 추가
    # 큐가 빌 때 까지
    q = deque()
    q.append((r, c))
    while q:
        tr, tc = q.popleft()  # 큐에서 좌표 하나 꺼냄
        k = t_br[tr][tc]  # 해당 좌표 값으로 길이 설정
        t_br[tr][tc] = 0  # 해당 좌표 0으로 만들기
        for i in range(1, k):
            for dr, dc in delta:
                nr, nc = tr + i * dr, tc + i * dc
                if 0 <= nr < h and 0 <= nc < w and t_br[nr][nc]:
                    q.append((nr, nc))


def adj_bricks(w: int, h: int, temp_br: list):
    # 블럭들 사이 빈공간 없애기
    stack = []
    # 행 방향 탐색
    for c in range(w):
        # 각 열을 위에서 아래로 탐색하면서
        # 0이 아닌 숫자를 스택에 넣고
        for r in range(h):
            if temp_br[r][c]:
                stack.append(temp_br[r][c])
        # 아래에서 위로 올라가면서 스택에서 하나씩 pop해서 입력
        # 스택이 비면 나머지 공간은 0으로 채우기
        for r2 in range(h - 1, -1, -1):
            if stack:
                temp_br[r2][c] = stack.pop()
            else:
                temp_br[r2][c] = 0


T = int(input())
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    result = []  # 남은 벽돌 "개수"를 저장할 리스트 -> 최소로 남은 개수만 출력하면 된다
    pos_list = []  # 공을 떨어뜨릴 위치들의 집합. 총 N 번 (0 ~ W-1)
    select_pos(N, W, H, pos_list)  # 공 떨어뜨릴 위치 생성

    # 벽돌 개수 중 최소값을 출력
    print(f'#{t} {min(result)}')

