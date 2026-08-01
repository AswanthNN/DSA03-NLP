import re
text = "My phone number is 9876543210 and my email is user@gmail.com"
phone = re.search(r"\d{10}", text)
if phone:
    print("Phone Number:", phone.group())
email = re.search(r"\S+@\S+", text)
if email:
    print("Email:", email.group())
words = re.findall(r"\bp\w+", text)
print("Words starting with 'p':", words)
