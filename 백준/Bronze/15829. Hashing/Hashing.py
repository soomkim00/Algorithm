# ord -> 문자를 기존에 할당되있는 숫자로 변환해주는..(부정확한 설명)
# ex. ord('a') = 97, ord('b') = 98

L = int(input())
string = list(input())
hash_val = 0

for i in range(len(string)):
    number = int(ord(string[i])) - 96
    hash_val += number * 31**i

print(hash_val % 1234567891)
