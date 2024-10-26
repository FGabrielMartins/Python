import socket

ports = [21,22,25,80,443,445,3306,8080]

for port in ports:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.2)
    code = client.connect_ex(("bancocn.com", port))
    if code == 0:
        print(port, "Porta Aberta")
    else:
        print(port, "Porta Fechada")

        