import re

password_regex = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#&])[A-Za-z\d@$!%*#&]{8,}$"

my_password = "aravindha1"

data = re.match(password_regex, my_password)

if data:
    print("valid")
else:
    print("invalid")


