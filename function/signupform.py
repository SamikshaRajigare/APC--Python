import re
def validate_email(email):
    pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9]+(\.[A-Za-z0-9]+)+\.[A-Za-z]{2,6}$'
    return bool(re.match(pattern, email))
print(validate_email("john.doe@example.com"))    
print(validate_email("user_name@test.org"))        
print(validate_email("abc123@my-domain.com"))      
print(validate_email("user@domain"))               
print(validate_email("@domain.com"))                             