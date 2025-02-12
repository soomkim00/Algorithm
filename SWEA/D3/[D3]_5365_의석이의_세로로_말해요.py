# 각 단어들 길이를 모은 리스트와, 그 중 최대값을 사용해서
# 총 탐색 반복 수와 해당 단어 이상의 경우 건너뛰게 설정

T = int(input())

for tc in range(1, T + 1):
    word_list = [list(input()) for _ in range(5)]

    len_list = [0] * 5
    for r in range(5):
        len_list[r] = len(word_list[r])

    result = []
    for c in range(max(len_list)):
        for r in range(5):
            if c >= len_list[r]:  # 탐색 위치가 단어의 길이보다 길면 넘어가
                continue
            else:
                result.append(word_list[r][c])

    print(f"#{tc} {''.join(result)}")
