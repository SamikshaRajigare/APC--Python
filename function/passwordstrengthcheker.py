import re
def check_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*()_-]', password):
        return False

    return True
print(check_password_strength("Password123!"))  
print(check_password_strength("password123!"))  
print(check_password_strength("PASSWORD123!")) 
print(check_password_strength("Password!"))     
print(check_password_strength("Pass123"))      