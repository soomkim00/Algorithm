import sys

sys.stdin = open("input.txt", "r")

# 행 방향, 열 방향 각각 순회하면서 체크
# 길이 변화하는 시점이 발생하면 경사로 체크
# 사전 체크사항 체크 후에
# 바로 이전에 down이 발생했었는가?를 기준으로 나눠서 체크


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N, X = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(N)]

        total = 0

        # 행 방향 탐색
        for r in range(N):
            cnt = 1  # 연속된 수의 개수
            down_check = False  # down 발생 체크
            for c in range(1, N):  # 두 번째부터 비교
                gap = board[r][c] - board[r][c - 1]  # 두 칸 사이의 차이
                # 높이 차이 2 이상이면 경사로 설치 불가
                if abs(gap) >= 2:
                    break

                # down 발생 시 현 지점 + X 가 범위를 벗어나면 불가능
                if gap == -1 and c + X - 1 >= N:
                    break

                # 높이가 같으면 진행
                if gap == 0:
                    cnt += 1

                # 바로 이전 down 발생 여부에 따른 경우를 나눠서 탐색
                # down 발생한 경우
                if down_check:
                    # down 이후 up: 경사로 2개 필요, down_check 해제
                    if gap == 1:
                        if cnt < 2 * X:
                            break
                        cnt = 1
                        down_check = False
                    # down 이후 down: 경사로 1개 필요
                    if gap == -1:
                        if cnt < X:
                            break
                        cnt = 1
                    # down 이후 벽: 경사로 1개 필요
                    if c == N - 1:
                        if cnt < X:
                            break
                # down 발생 안 한 경우
                else:
                    # up: 경사로 1개 필요
                    if gap == 1:
                        if cnt < X:
                            break
                        cnt = 1
                    # down: down_check 갱신
                    if gap == -1:
                        down_check = True
                        cnt = 1
            # break 한 번도 없었으면..! 활주로 가능
            else:
                total += 1

        # 열 방향 탐색.. 똑같이!
        for c in range(N):
            cnt = 1  # 연속된 수의 개수
            down_check = False  # down 발생 체크
            for r in range(1, N):  # 두 번째부터 비교
                gap = board[r][c] - board[r - 1][c]  # 두 칸 사이의 차이
                # 높이 차이 2 이상이면 경사로 설치 불가
                if abs(gap) >= 2:
                    break

                # down 발생 시 현 지점 + X 가 범위를 벗어나면 불가능
                if gap == -1 and r + X - 1 >= N:
                    break

                # 높이가 같으면 진행
                if gap == 0:
                    cnt += 1

                # 바로 이전 down 발생 여부에 따른 경우를 나눠서 탐색
                # down 발생한 경우
                if down_check:
                    # down 이후 up: 경사로 2개 필요, down_check 해제
                    if gap == 1:
                        if cnt < 2 * X:
                            break
                        cnt = 1
                        down_check = False
                    # down 이후 down: 경사로 1개 필요
                    if gap == -1:
                        if cnt < X:
                            break
                        cnt = 1
                    # down 이후 벽: 경사로 1개 필요
                    if r == N - 1:
                        if cnt < X:
                            break
                # down 발생 안 한 경우
                else:
                    # up: 경사로 1개 필요
                    if gap == 1:
                        if cnt < X:
                            break
                        cnt = 1
                    # down: down_check 갱신
                    if gap == -1:
                        down_check = True
                        cnt = 1
            # break 한 번도 없었으면..! 활주로 가능
            else:
                total += 1

        print(f"#{tc} {total}")
