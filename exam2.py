#별찍기 예제2

num = int(input())

for i in range(1,num+1):
    print(" "*(num+1-i) + "*"*i)