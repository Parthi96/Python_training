
import re

madText = open('madText.txt', 'w')

text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

madText.write(text)
madText.close()
content = re.split('(\W+)', text)

for i in content:
    if i == 'NOUN':
        content.insert(content.index('NOUN'), input('enter the ' + i + ': '))
        content.remove('NOUN')
    elif i == 'VERB':
        content.insert(content.index('VERB'), input('enter the ' + i + ': '))
        content.remove('VERB')
    elif i == 'ADVERB':
        content.insert(content.index('ADVERB'), input('enter the ' + i + ': '))
        content.remove('ADVERB')
    elif i == 'ADJECTIVE':
        content.insert(content.index('ADJECTIVE'), input('enter the ' + i + ': '))
        content.remove('ADJECTIVE')

content = ''.join(content)
print(content)
madLibs = open('madText2.txt', 'w')
madLibs.write(content)
madLibs.close()