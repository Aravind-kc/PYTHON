import re

password_regex = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#&])[A-Za-z\d@$!%*#&]{9,}$"

my_password = "aravind@1"

data = re.match(password_regex, my_password)

if data:
    print("valid")
else:
    print("invalid")


