#백준 상근날드
min_burger = int(input())
jung = int(input())
if jung<min_burger:
    min_burger = jung
ha = int(input())
if ha<min_burger:
    min_burger=ha
coke = int(input())
soda = int(input())
if coke < soda :
    drink = coke
else :
    drink = soda

set = min_burger + drink -50
print(set)