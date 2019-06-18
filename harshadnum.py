def isharshad(num) :  
  num1 = int(num[0])
  num2 = int(num[1])
  sum = num1 + num2
  if (int(num)%sum == 0) :
    print('its a harshad number')
  else :  
    print('its not a harshad number')

print('enter a number with base 10')
num = str(input())
isharshad(num)