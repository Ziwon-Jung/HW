#백준 10871번 문제

a = input( )
m,n=a.split(' ')
m = int(m)
n = int(n)
num = input()
num= num.split(' ')
answer = ''
for i in range(m):
    if int(num[i]) <n:
        answer += num[i] + ' '

print(answer)
