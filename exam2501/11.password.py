import string
def contain_lower(password):
    for ch in password:
        if ch.islower():
            return True
    return False

def contain_upper(password):
    for ch in password:
        if ch.isupper():
            return True
    return False

def contains_number(password):
    for ch in password:
        if ch.isnumeric():
            return True
    return False

def contains_special(password):
    special_char=string.punctuation
    for ch in password:
        if ch in special_char:
            return True
    return False

def strength_check(password):
    if(len(password)>=8 and contain_lower(password) and contain_upper(password) and contains_number(password) and contains_special(password)):
        print("STRONG PASSWORD")
    else:
        print("WEAK PASSWORD")

password=input("enter the password: ")
strength_check(password)
