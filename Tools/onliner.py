import websocket, threading, random, json, time, sys
import pystyle
from pystyle import *
def main():
    config = {
        "details": "discord.gg/techbeams",
        "state": "get beamed",
        "name": "Wrath Multitool",
    }


    class Onliner:
        def __init__(self, token) -> None:
            self.token    = token
            self.statuses = ["online", "idle", "dnd"]

        def __online__(self):
            ws = websocket.WebSocket()
            ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
            response = ws.recv()
            event = json.loads(response)
            heartbeat_interval = int(event["d"]["heartbeat_interval"]) / 1000
            ws.send(
                json.dumps(
                    {
                        "op": 2,
                        "d": {
                            "token": self.token,
                            "properties": {
                                "$os": sys.platform,
                                "$browser": "RTB",
                                "$device": f"{sys.platform} Device",
                            },
                            "presence": {
                                "game": {
                                    "name": config["name"],
                                    "type": 0,
                                    "details": config["details"],
                                    "state": config["state"],
                                },
                                "status": random.choice(self.statuses),
                                "since": 0,
                                "activities": [],
                                "afk": False,
                            },
                        },
                        "s": None,
                        "t": None,
                    }
                )
            )

            print(Colorate.Horizontal(Colors.red_to_green, f"Logged in | {self.token}"))

            while True:
                heartbeatJSON = {
                    "op": 1, 
                    "token": self.token, 
                    "d": "null"
                }
                ws.send(json.dumps(heartbeatJSON))
                time.sleep(heartbeat_interval)




    import tkinter as tk
    from tkinter.filedialog import askopenfilename

    tk.Tk().withdraw()  # part of the import if you are not using other tkinter functions
    fn = askopenfilename(title=("Open a Token file"), filetypes=(("Text Files", "*.txt"),))



    for token in open(fn,'r').read().splitlines():
        threading.Thread(target=Onliner(token).__online__).start()