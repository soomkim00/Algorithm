import sys

sys.stdin = open("input.txt", "r")


def decode(r, c, n):
    sr, sc = r, c

    # 암호문 해독
    # 우선 한 숫자의 길이를 구해야 한다
    # 역순탐색하면서 순서대로 1 > 0 > 1 > 0 으로 바뀌는 세 부분의 길이를 구한 후
    # 가장 짧은 길이가 단어의 비율 1에 해당
    # 세 부분의 길이 비율로 숫자도 구할 수 있고, 암호문의 총 길이도 구할 수 있다
    answer = []
    width = 0
    tc = c
    section = 0
    while len(answer) < 8:
        width_list = [0, 0, 0]
        check = 0
        nc = tc
        while True:
            width_list[check] += 1
            nc -= 1
            if check % 2 == 0 and bin_arr[r][nc] == '0':
                check += 1
            elif check == 1 and bin_arr[r][nc] == '1':
                check += 1
            if check == 3:
                break
        # print(width_list)
        if width == 0:  # width 안구했으면 한번만 구하자
            # 총 길이는 최소 길이 * 7(한 숫자에 7 비트) * 8(숫자 개수)
            section = min(width_list)
            width = section * 7 * 8
        tc -= section * 7

        if min(width_list) > 1:
            n = min(width_list)
            for i in range(3):
                width_list[i] = int(width_list[i] / n)
        width_list.reverse()
        answer.append(ratio[str(width_list)])

    # 암호문의 세로 길이를 구하기
    # 최소 세로 길이가 5이므로 4칸 밑부터 검사해서
    # 0이 나올때까지의 높이를 측정
    height = 4
    while True:
        if r + height >= n or bin_arr[r + height][c] == '0':
            break
        height += 1

    # 시작점부터 가로 세로 길이만큼 방문처리. 처리한 곳은 체크 안하도록
    for h in range(height):
        for w in range(width):
            visited[sr + h][sc - w] = 1

    answer.reverse()
    print(answer)
    sum1 = sum2 = 0
    for i in range(0, 8, 2):
        sum1 += answer[i] * 3
        sum2 += answer[i + 1]

    if (sum1 + sum2) % 10 == 0:
        result.append(sum(answer))


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()[:M]) for _ in range(N)]

    # 16진수 -> 2진수 변환 딕셔너리
    hex_to_bin = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
                  "4": "0100", "5": "0101", "6": "0110", "7": "0111",
                  "8": "1000", "9": "1001", "A": "1010", "B": "1011",
                  "C": "1100", "D": "1101", "E": "1110", "F": "1111",
                  }

    ratio = {"[2, 1, 1]": 0, "[2, 2, 1]": 1,
             "[1, 2, 2]": 2, "[4, 1, 1]": 3,
             "[1, 3, 2]": 4, "[2, 3, 1]": 5,
             "[1, 1, 4]": 6, "[3, 1, 2]": 7,
             "[2, 1, 3]": 8, "[1, 1, 2]": 9
             }

    # 2진수 테이블 생성
    bin_arr = []
    for r in range(N):
        temp = []
        for c in range(M):
            temp.append(hex_to_bin[arr[r][c]])
        bin_arr.append(''.join(temp))

    # 암호가 여러개 있을 수 있어서
    # 암호 한번 체크하면 길이만큼 다음에 탐색을 안하겠다
    # 방문 확인 테이블
    visited = [[0] * len(bin_arr[0]) for _ in range(N)]
    # 2진수 테이블을 탐색
    # 열 역방향 순회
    result = []
    for r in range(N):
        for c in range(len(bin_arr[0]) - 1, -1, -1):
            if not (visited[r][c]) and bin_arr[r][c] == '1':
                decode(r, c, N)

    print(f"#{tc} {sum(result)}")
