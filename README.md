# faulty calculator
# this program will calculate numaric value 
# if this calculator used by student it will give some wrong result becouse of cheater student 
num1 = int(input("enter 1st value: "))
num2 = int(input("enter 2nd value: "))
operator = input("chose your operator *,+,/: ")
if num1==45 and num2==5 and operator=='*':
    print('555')
elif num1==56 and num2==9 and operator=='+':
    print('77')
elif num1==56 and num2==6 and operator=='/':
    print('4')
elif operator=='*':
    mul = num1*num2
    print(mul)
elif operator=='+':
    add = num1+num2
    print(add)
elif operator=='/':
    div = num1/num2
    print(div)
else:
    print("Error try again!")
