import json
from sendEmail import send_emails
filename = './data/data.json'

# Open and load the JSON data

with open(filename, 'r') as file:
    email_list = json.load(file)


if __name__ == '__main__':
    result = send_emails(email_list,'הגשת מועמדות - מפתחת תוכנה מנוסה','','./data/Tamar Berman - CV.docx','./data/Tamar Berman - CV.pdf')
    print(f"success : {result[0]}")
    print(f"unsuccess : {result[1]}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
