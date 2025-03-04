# 완전 이진 트리다
# - 1~N 까지의 인덱스를 가지는 트리(값 아님. 노드 번호!)
# - 노드 번호 i인 노드의 왼쪽/ 오른쪽 자식 노드 번호 : 2*i / 2*i+1 (완전이진트리 성질)
# 노드 번호를 인덱스로 사용하는 N+1크기(0  사용 x)의 배열을 선언해서 트리로 사용하고
# 해당 트리를 중위순회하면서 방문 순서대로 번호를 매기면 원하는 트리 결과가 나온다.
# 이후 루트는 index 1인 값(1번 노드) N//2번 노드는 index가 N//2인 값

def inorder_traverse(i):
    global num
    if i > N:
        return
    inorder_traverse(2 * i)
    tree[i] = num
    num += 1
    inorder_traverse(2 * i + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    num = 1
    inorder_traverse(1)

    print(f"#{tc} {tree[1]} {tree[N // 2]}")
