import re
text = 'My number is 123-4567-8901.'
phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')
phone = phoneNumber.search(text)

print('Phone Number STD code is ' + phone.group(1))
print('Phone Number without STD is ' + phone.group(2))
print('Phone Number with STD code is ' + phone.group())