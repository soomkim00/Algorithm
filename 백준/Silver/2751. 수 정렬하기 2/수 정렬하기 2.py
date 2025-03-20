import sys

if __name__ == "__main__":
    N = int(input())
    po_li = []
    ng_li = []
    for _ in range(N):
        num = int(sys.stdin.readline().strip())
        if num >= 0:
            po_li.append(num)
        else:
            ng_li.append(num)
    po_li.sort()
    ng_li.sort()
    for n in ng_li:
        print(n)
    for n in po_li:
        print(n)
