name = ''
while name != 'Parthi' :
  print('Who are you ?')
  name=input()
  if name != 'Joe' :
    continue
  else :
     print('Hello, Joe, What is the password ? (hint: its a  fish)')
     password = input()
  if password == 'swordfish':
     break     
  else :
     continue
print('Access granted.')     
