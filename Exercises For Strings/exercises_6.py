import re
email_address = input('enter the email address :')
pattern = r"[^@]+@[^@]+\.[^@]"   
match = re.match(pattern, email_address)
if match:
  print("Valid")
else:
  print("invalid ")

