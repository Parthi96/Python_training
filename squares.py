def square(num):
  dict={x:x*x for x in range(1,num+1)} 
  print(dict)

print('enter the number')
num =int(input())
square(num)
