import sys

sys.stdin = open("input.txt", "r")

# dp를 사용해보자
# 각 정류장까지 가는데 들어가는 최소시간들을 리스트로 만들어 놓음
# 시작지점부터 최소 교환 횟수를 갱신
# 이후의 최대값을 보장하는가?
# 정류장의 개수 출발지~도착지 : N-1개


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        data = list(map(int, input().split()))
        N = data[0]
        data = data[1:]  # 정류장 번호 0 ~ N-2, N-1은 도착지라 정보 없음
        dp = [float('inf')] * (N - 1)
        print(dp)

        print(f"#{tc}")


# 있잖아. 나 처음에 -1로 안 넣고 엉뚱한데 고치다가 코드 개 꼬엿.
#