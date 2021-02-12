import re


open_file = open('existing-contacts.txt', 'r')
emails = re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
phone = re.findall(r'\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}')
print(emails)
print(phone)


match_email = []
match_phone = []









# print(extract)

