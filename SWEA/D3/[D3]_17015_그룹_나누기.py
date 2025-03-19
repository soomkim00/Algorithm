import sys

sys.stdin = open("input.txt", "r")

# 신청서 정보 == 그래프 간선 정보
# 총 몇 개의 그래프가 그려지는가?
# 연결리스트로 그래프 정보 받고
# 각 노드들부터 탐색하면서 이미 탐색한 노드는 visited 처리
# visited 안 된 노드부터 다시 탐색 시작
# 총 탐색 횟수 == 그래프의 개수

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        paper = list(map(int, input().split()))

        # 입력 정보로 연결 리스트 생성
        adj_li = [[] for _ in range(N + 1)]  # 0 버림
        for i in range(0, 2 * M, 2):
            # 무향(혹은 양방향)그래프 -> 앞 뒤 바꿔서 두 번 추가
            adj_li[paper[i]].append(paper[i + 1])
            adj_li[paper[i + 1]].append(paper[i])

        # 각 노드들을 탐색. 이미 탐색한 노드 탐색 x
        # stack을 사용한 dfs
        visited = [0] * (N + 1)  # 각 노드 방문 여부, 0 버림
        stack = []
        cnt = 0  # 트리 개수
        for i in range(1, N + 1):  # 1~N 노드 탐색
            if visited[i]:  # 해당 노드 탐색한 경우 더 이상 탐색 x
                continue
            cnt += 1  # 탐색 시작할때마다 개수 1 증가
            stack.append(i)
            while stack:
                now = stack.pop()
                if not visited[now]:
                    visited[now] = 1
                    for next in adj_li[now]:
                        if not visited[next]:
                            stack.append(next)

        print(f"#{tc} {cnt}")
