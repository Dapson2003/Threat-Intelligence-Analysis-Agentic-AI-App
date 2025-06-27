import socket

domain = "Google.com"
ip_address = socket.gethostbyname(domain)
open("./IP_Domain_intelligence/log.txt", "a").write(f"Resolved {domain} -> {ip_address}\n")
print(f"Resolved {domain} -> {ip_address}\n")