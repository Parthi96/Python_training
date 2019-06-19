import re


print("\nThis program searches for lines with your string in them\n")
search_str = input("Please write the string you are searching for: \n")
print("")

file = open("\\Users\pnavanee\Devops assignment\Devops.txt","r")

content = file.read()
file.close()
for line in content(content, search_str):
    print(line)

regex = re.compile(r".*(%s).*" % search_str)


if regex.search(content) is None:
    print("No matches was found.")
else:
    print(regex.findall(content))
