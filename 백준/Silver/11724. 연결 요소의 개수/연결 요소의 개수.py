import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        parent[rb] = ra             # 한 쪽 루트만 연결

def solve():
    N, M = map(int, input().split())
    # 1. 초기화: 각 정점은 자기 자신이 루트
    global parent
    parent = list(range(N + 1))

    # 2. 입력마다 union
    for _ in range(M):
        u, v = map(int, input().split())
        union(u, v)

    # 3. 서로 다른 루트 개수 세기
    roots = set()
    for i in range(1, N + 1):
        roots.add(find(i))

    print(len(roots))

if __name__ == "__main__":
    solve()
