import socket

domain = "Google.com"
ip_address = socket.gethostbyname(domain)
open("log.txt", "a").write(f"Resolved {domain} -> {ip_address}\n")
print(f"Resolved {domain} -> {ip_address}\n")