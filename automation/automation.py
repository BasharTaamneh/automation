import re

# with open("automation/potential-contacts.txt", "r") as f:
#     email_content = f.read().split(" ")

# emails = ""
# for i in email_content:
#     pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]'
#     sequence = i
#     if re.match(pattern, sequence):
#         emails += "{} ".format(i) 
#     else: pass
# emails = sorted(emails.split(" "))

# with open("automation/emails.txt", "w+") as f:
#     for email in emails:
#         f.write("{}\n".format(email))

#////////////////////////////////////////////////////////////////////////////////

with open("automation/potential-contacts.txt", "r") as f:
    phone_content = f.read().split(" ")

# print(phone_content)
phones = ""
for i in phone_content:
    pattern = r"^\D*(?:\d\D*){10,}$"
    sequence = i
    if re.search(pattern, sequence):
        # print(i)
        phones += "{} ".format(i) 
    else: pass
phones = sorted(phones.split(" "))

# for i in phones:
#     if len(i.split(".")) == 2:
#         first = i.split(".")[1]
#     elif len(i.split(".")) == 1:
#         first = i
#     print(first)
print(phones)
