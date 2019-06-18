def sequence(num) :
  list = num.split(',') 
  tup = tuple(list) 
  print('list :',list)
  print('tuple :', tup)

print('enter the sequence')
num = input()
sequence(num)
