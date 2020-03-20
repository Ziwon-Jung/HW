#백준 2523번
num = int(input())

for i in range(1,num):
    print("*"*i)
for i in range(num,0,-1):
    print("*" * i)