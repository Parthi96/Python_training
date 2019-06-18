print('enter name')
name = input()
print('enter age')
age = int(input())
if name == 'Alice' : 
  print('hi, Alice.')
elif age < 12:
  print('you are not Alice, kiddo')
elif (age > 100) and (age <2000 ):
  print('you are not Alice, grannie.')   
else :
  print('Unlike you, alice is not undead, immortal vampire.')      