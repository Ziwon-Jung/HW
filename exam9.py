#팩토리얼
def factorial(num) :
    if num ==1 or num==0 :
        return 1
    else:
        return factorial(num-1)*num

num = int(input())
print(factorial(num))
