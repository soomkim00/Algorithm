import sys

sys.stdin = open("input.txt", "r")

# 재귀를 사용한 부분집합 생성
# 부분집합의 합만 K와 같은지 비교하면 되기 때문에, 집합 정보가 아닌 누적 합(temp)만 전달
# 현재 고른 원소의 개수 == 다음 고를 원소의 idx 이므로, cnt 변수 하나로 개수와 인덱스 동시 처리


def recur(cnt, temp):
    global result

    # 현재 합이 목표와 같아지면 result 증가, return으로 탐색 종료
    if temp == K:
        result += 1
        return

    # 모두 찾은 경우 탐색 종료
    if cnt == N:
        return

    # 선 가지치기: 호출 전에 검사해서 호출 자체를 줄이면, 조금 시간이 줄어든다
    if temp + arr[cnt] <= K:
        recur(cnt + 1, temp + arr[cnt])  # cnt번째 원소를 고르는 경우
    recur(cnt + 1, temp)  # cnt번째 원소를 고르지 않는 경우


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T + 1):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        result = 0
        selected = [0] * N
        recur(0, 0)

        print(f"#{tc} {result}")
