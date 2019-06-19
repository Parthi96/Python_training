import glob
import re
files = glob.glob('*.py')
print(files)

text = input('input the string : ')

for file in files :
   for line in open(file):
      for string in line.split():        
        matched = re.search(text,line)
        if matched:
          print(matched)

