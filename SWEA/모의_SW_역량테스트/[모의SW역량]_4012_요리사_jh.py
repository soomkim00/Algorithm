def check_point(A, B):
    global min_v

    length = N // 2
    point_A = point_B = 0
    for i in range(length):
        for j in range(length):
            if i != j:
                point_A += table[A[i]][A[j]]
                point_B += table[B[i]][B[j]]

    min_v = min(min_v, abs(point_A - point_B))
    return


def make_food(idx, select, cnt=0):
    if (N // 2) - cnt > (N - 1) - idx:
        return
    if cnt == (N // 2):
        A = []
        B = []
        for i in range(N):
            if select[i] == 1:
                A.append(i)
            else:
                B.append(i)

        check_point(A, B)
        return

    select[idx] = 1
    make_food(idx + 1, select, cnt + 1)
    select[idx] = 0
    make_food(idx + 1, select, cnt)


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        table = [list(map(int, input().split())) for _ in range(N)]
        min_v = float("inf")

        select = [0] * N
        make_food(0, select)
        print(f"#{tc} {min_v}")