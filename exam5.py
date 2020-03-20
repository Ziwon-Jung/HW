#백준 bronze 9325번 문제
a = int(input())

for i in range(a):
    price = int(input())
    b = int(input())
    for j in range(b):
        option = input()
        m,n = option.split(' ')
        price += int(m)*int(n)
    print(price)
