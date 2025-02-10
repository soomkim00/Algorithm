def is_sudoku(sudoku):
    # 3x3 안 중복 확인
    # 각 칸 첫 번째 칸 기준(0,0), (3,0), (0,3) ...
    # 아홉칸씩 비교 중복이면 바ㅏㅏ로 return
    for i in range(0, SIZE, 3):
        for j in range(0, SIZE, 3):
            temp = []
            for di in range(3):
                for dj in range(3):
                    if sudoku[i + di][j + dj] in temp:
                        return 0
                    temp.append(sudoku[i + di][j + dj])

    # 같은 줄 중복 확인
    # 행 기준 열 증가 반복
    # 열 기준 행 증가 반족
    # 걸리면 return 하는거야~
    for n in range(SIZE):
        temp = []
        for j in range(SIZE):
            if sudoku[n][j] in temp:
                return 0
            temp.append(sudoku[n][j])
        temp.clear()
        for i in range(SIZE):
            if sudoku[i][n] in temp:
                return 0
            temp.append(sudoku[i][n])

    # 살아남았으면 return 1
    return 1


T = int(input())
SIZE = 9

for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(SIZE)]

    print(f"#{tc} {is_sudoku(sudoku)}")
