import requests;
import socket
import time;

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


channel_id = None;
bot_token = None;

with open("config.txt", "r") as text:

    content = text.readlines();

    channel_id = content[0].split("=")[1].rstrip();
    bot_token = content[1].split("=")[1].rstrip();


prev_address = None;

while True:

    time.sleep(3);

    internet = False;

    try:
        req = requests.get('http://clients3.google.com/generate_204')
        if req.status_code == 204:
            internet = True;
    except:
        1;

    if internet == False:
        continue;

    address = get_ip();

    if prev_address != address:
        requests.post("https://discord.com/api/v9/channels/" + channel_id + "/messages", headers={
                "Accept": "*/*",
                "Content-Type": "application/json",
                "Authorization": bot_token,
            },
            json={"content":address},
        )

        prev_address = address;
