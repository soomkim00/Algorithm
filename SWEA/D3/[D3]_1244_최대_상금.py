import sys

sys.stdin = open("input.txt", "r")


def solve():
    T = int(input())

    for tc in range(1, T + 1):
        data, change = map(int, input().split())
        data = list(str(data))

        max_v = 0  # 최대값
        memo = set()  #

        def recur(cnt, temp: list):
            nonlocal max_v
            # 종료조건 교환 횟수 다 차면 최대값 비교/갱신
            if cnt == change:
                max_v = max(max_v, int(''.join(temp)))
                return

            # 메모이제이션
            # 이 교환 횟수에서 이 상태가 나왔으면 더 이상 진행 x
            if (cnt, tuple(temp)) in memo:
                return
            # 교환 횟수, 상태 저장
            memo.add((cnt, tuple(temp)))

            # 재귀호출
            # 서로 다른 모든 경우의 수를 교환
            for i in range(len(data) - 1):
                for j in range(i + 1, len(data)):
                    # 교환
                    temp[i], temp[j] = temp[j], temp[i]
                    recur(cnt + 1, temp)
                    # 원상복귀
                    temp[i], temp[j] = temp[j], temp[i]

        recur(0, data)
        print(f'#{tc} {max_v}')


if __name__ == "__main__":
    solve()

"""
#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645
"""
