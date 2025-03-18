import sys

sys.stdin = open("input.txt", "r")


def make(cnt, total):
    global result

    # n 번의 선택을 다 했으면 최소값 갱신
    if cnt == N:
        result = min(result, total)
        return

    # i는 공장 번호, cnt는 재귀의 깊이==제품 번호
    for i in range(N):
        # 같은 공장 한번만 선택하기 위해서 방문 여부 체크
        if not visited[i]:
            # i 번 공장 사용
            visited[i] = 1
            # 가지치기. 다음 합이 최소값보다 작을때만 탐색
            if total + V[cnt][i] <= result:
                # 선택한 정보와 cnt제품의 i번째 공장 비용을 더한 값으로 호출
                make(cnt + 1, total + V[cnt][i])
            # i 번 공장 선택 취소
            visited[i] = 0


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        V = [list(map(int, input().split())) for _ in range(N)]

        result = float('inf')
        visited = [0] * N

        make(0, 0)

        print(f"#{tc} {result}")
