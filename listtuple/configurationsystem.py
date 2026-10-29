server_ip = (192, 168, 1, 10)
allowed_ips = ["192.168.1.2", "192.168.1.3"]  

def update_allowed_ips():
    print("Current Allowed IPs:", allowed_ips)
    
    ip = input("Enter new IP to allow: ")
    allowed_ips.append(ip)
    
    print("Allowed IP added successfully!")

print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)

update_allowed_ips()

print("\nUpdated Configuration:")
print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)