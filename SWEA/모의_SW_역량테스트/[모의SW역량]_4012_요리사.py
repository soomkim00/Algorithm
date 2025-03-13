import sys

sys.stdin = open("input.txt", "r")

# 비트연산으로 A, B에 쓸 재료를 고르자 (N개 원소)
# 진행 중 cnt가 N//2인 경우에 점수 계산
# 이중 for문으로 발견되는 서로 다른 두 원소들에 대해서 Sij, Sji를 더한다
# 0에 대해서도 똑같이 더하고 차이를 구한 후
# 기존의 차이와 비교해서 최소값을 구한다
# ---- 완전탐색 완료. 가지치기 시도 ----
# 시도 1. 비트 생성 시 최소/최대값 설정 -> 반복수 감소 미미..
# 실패
# 시도 2. 중복 연산 제거 -> 기존 사용했던 인덱스와 반대되는 인덱스가 등장하면 중복계산 -> 기존 정보 저장이 오히려 더 오래걸림
# 실패
# 시도 3. A, B가 서로 반대여도 똑같은 결과다 -> 비트 탐색 시 index 0이 무조건 들어간다고 판단 -> 연산 반으로 줄어듬

T = int(input())


# 요리해서 점수를 비교하자
def cook(li: list):
    global result
    a_score, b_score = 0, 0  # 두 요리의 점수

    # boolean 리스트로 A음식에 포함된 식재료를 표시 (True면 A, False면 B)
    sel = [False] * N
    for idx in li:
        sel[idx] = True

    # i < j인 모든 쌍에 대해 두 재료가 모두 A 혹은 모두 B에 속하면 시너지 합을 계산
    for i in range(N):
        for j in range(i + 1, N):
            if sel[i] and sel[j]:
                a_score += arr[i][j] + arr[j][i]
            elif not sel[i] and not sel[j]:
                b_score += arr[i][j] + arr[j][i]

    result = min(result, abs(a_score - b_score))


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # if tc != 1:
    #     continue
    result = float('inf')  # 비교할 최소 차이

    # 비트연산으로 N개 중 N/2개를 고른 경우를 만들자
    for i in range(0x1 << N):
        # 0번째 원소가 1인 경우만 탐색하겠다
        if not(i & 0x1):
            continue
        cnt = 0  # 몇 개를 골랐는가(1인가)를 체크
        temp = []  # 사용할 원소들의 index를 저장할 리스트
        for j in range(N):
            if i & (0x1 << j):  # 오른쪽에서 j번째 원소가 1인가?
                temp.append(j)
                cnt += 1
        if cnt == N // 2:  # 원소가 N//2개가 골라졌으면
            cook(temp)  # 요리해서 점수를 비교하자

    print(f"#{tc} {result}")

"""
#1 2
#2 1
#3 38
#4 15
#5 4
#6 0
#7 51
#8 23
#9 13
#10 11
"""
