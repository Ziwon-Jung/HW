#백준 bronze 9085번 문제
a = int(input())

for i in range(a):
    b = int(input())
    total = 0
    c = input()
    numlist = c.split(' ')
    for j in range(b):
        total += int(numlist[j])
    print(total)