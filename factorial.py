def factorial(num) :
 fact = 1
 while num>0 :
  fact = fact * num
  num = num - 1
 print(fact) 

print('enter the number')
num = int(input())
factorial(num)
