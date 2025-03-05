# 주어진 정보를 각 인덱스 노드의 알파벳과, 좌/우 노드 번호로 저장
# 인덱스 기반 접근하기때문에 노드 번호-1을 사용한다
# 루트 노드를 0으로 시작, left와 right를 부를 때도 -1 값으로..!


def inorder(n: int):
    if left[n]:
        inorder(left[n] - 1)
    result.append(alpha[n])
    if right[n]:
        inorder(right[n] - 1)


for t in range(1, 11):
    N = int(input())
    alpha = [0] * (N)
    left = [0] * (N)
    right = [0] * (N)
    result = []

    # 입력값을 글자, 왼쪽노드, 오른쪽 노드로 나눠서 저장
    for i in range(N):
        temp = list(input().split())
        alpha[i] = temp[1]
        if len(temp) > 2:
            left[i] = int(temp[2])
        if len(temp) > 3:
            right[i] = int(temp[3])

    # 재귀를 사용한 중위순회
    inorder(0)

    print(f"#{t} {''.join(result)}")
