import re

stripChar = input('Enter character to strip: ')
context = input('Enter string to strip: ')
stripContext = None


def strip(char, string):
    if char == "":               
        regsp = re.compile(r'^\s+|\s+$')
        stripContext = regsp.sub("", context)
        return stripContext
    else:                   
        stripContext = re.sub(r'^{}+|{}+$'.format(char,char), "", strip("",string))
        return stripContext

print(strip(stripChar, context))