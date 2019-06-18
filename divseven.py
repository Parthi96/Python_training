def divseven():
  m=[]
  x = range(2000,3201)
  for n in x :
    if (n % 7 == 0) and (n % 5 != 0) :
      m.append(n)
    else :  
      continue
  print(m)    

print('numbers divisible by 7 and are not mutiple of 5')
divseven()      