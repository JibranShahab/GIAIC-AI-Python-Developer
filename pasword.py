# create pasword strength.
import re

def checkpasword_strenght(password):
    if len(password) < 8:
        return "weak: password must be atleast 8 characters long."
    # elif len(password) >= 8:
    #     return "strong: password"
    
    # else:
    #     print("strong")
    if not re.search('[A-Z]', password):
        return "weak: password at least one upepercase letter "
    
    if not re.search('[a-z]', password):
        return "weak: password at least one ;lowercase letter. "

    if not re.search('[0-9]', password):
        return "weak: password at least one digit. "

    if not re.search('[/?<>@#%&!;":,()[{}]]',password):
        return "strong: password. "


password = input("enter a password" " ")
result = checkpasword_strenght(password)
print(result)
