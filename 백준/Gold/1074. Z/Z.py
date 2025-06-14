import sys

input = sys.stdin.readline


def solve():
    N, r, c = map(int, input().split())

    s_r, s_c = 0, 0
    cnt = 0
    # print('s_r, s_c, cnt, N')
    while True:
        # print(s_r, s_c, cnt, N)
        if s_r == r and s_c == c:
            print(cnt)
            return

        m_r, m_c = s_r + 2 ** (N - 1), s_c + 2 ** (N - 1)
        z = 0

        if c >= m_c and r < m_r:
            z = 1
            s_c = m_c
        elif c < m_c and r >= m_r:
            z = 2
            s_r = m_r
        elif c >= m_c and r >= m_r:
            z = 3
            s_r = m_r
            s_c = m_c

        cnt += z * (4 ** (N - 1))
        N -= 1


if __name__ == '__main__':
    solve()
