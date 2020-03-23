#백준 1075번
n= int(input())
f = int(input())

num = (n//100) * 100
cnt =0
for i in range(100):
    if num % f == 0:
        break;
    else:
        num += 1
        cnt += 1

if cnt <10 :
    print('%02d' %cnt)
else:
    print(cnt)
