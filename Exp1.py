import re
text = "My phone number is 9876543210 and my email is user@gmail.com"
# Search for a phone number
phone = re.search(r"\d{10}", text)
if phone:
    print("Phone Number:", phone.group())
# Search for an email
email = re.search(r"\S+@\S+", text)
if email:
    print("Email:", email.group())
# Find all words starting with 'p'
words = re.findall(r"\bp\w+", text)
print("Words starting with 'p':", words)
