import re


def extract_contacts(file_path):

    phone_numbers = []
    finall_phone_numbers = []

    with open(file_path, "r") as f:
        email_content = f.read().split(" ")

    emails = ""
    for i in email_content:
        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]"
        sequence = i
        if re.match(pattern, sequence):
            emails += "{} ".format(i)
        else:
            pass
    emails = sorted(emails.split(" "))

    with open("automation/emails.txt", "w+") as f:
        for email in emails:
            f.write("{}\n".format(email))

    # ***************************************************************************************//

    with open(file_path, "r") as f:
        numbers = f.read()

    match_num_1 = re.findall("\d{10}", numbers)
    for phone_num in match_num_1:
        phone_num = "206-" + phone_num[:3] + "-" + phone_num[3:6] + "-" + phone_num[6:]
        phone_numbers.append(phone_num)

    match_num_2 = re.findall("\(\d{3}\)\d{3}[-.]\d{4}", numbers)
    for phone_num in match_num_2:
        phone_num = "206-" + phone_num[1:4] + "-" + phone_num[5:8] + "-" + phone_num[9:]
        phone_numbers.append(phone_num)

    match_num_3 = re.findall("\d{3}[-.]\d{3}[-.]\d{4}", numbers)
    for phone_num in match_num_3:
        phone_num = "206-" + phone_num[:3] + "-" + phone_num[4:7] + "-" + phone_num[8:]
        phone_numbers.append(phone_num)

    phone_match_area_code_format_2 = re.findall(
        "[+]\d{1}[-.]\d{3}[-.]\d{3}[-.]\d{4}", numbers
    )
    for phone_num in phone_match_area_code_format_2:
        phone_num = "206-" + phone_num[3:]
        phone_numbers.append(phone_num)

    phone_match_area_code_format_1 = re.findall(
        "\d{3}[-.]\d{3}[-.]\d{3}[-.]\d{4}", numbers
    )
    for phone_num in phone_match_area_code_format_1:
        phone_num = phone_num
        phone_numbers.append(phone_num)

    # Removi Duplicates
    phone_numbers = list(dict.fromkeys(phone_numbers))
    # Sorting
    phone_numbers.sort()

    for i in phone_numbers:
        finall_phone_numbers.append(i[4:16])

    # print(len(findall_phone_numbers))
    # print(findall_phone_numbers)
    # print(phone_numbers)
    # print(len(phone_numbers))
    
    with open("automation/phone_numbers.txt", "w+") as f:
        for phone_num in finall_phone_numbers:
            phone_num = phone_num + "\n"
            f.write(phone_num)

    finall_phone_numbers = []
    return phone_numbers


print(extract_contacts("automation/potential-contacts.txt"))
