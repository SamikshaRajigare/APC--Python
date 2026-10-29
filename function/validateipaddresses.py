import re
def validate_ip(ip):
    ipv4_pattern = (
        r'^('
        r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.'
        r'){3}'
        r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
    )
    ipv6_pattern = (
        r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    )

    if re.match(ipv4_pattern, ip):
        return True
    if re.match(ipv6_pattern, ip):
        return True

    return False
print(validate_ip("192.168.1.1"))
print(validate_ip("255.255.255.255"))
print(validate_ip("256.168.1.1"))
print(validate_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
print(validate_ip("2001:db8::7334"))