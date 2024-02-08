import requests;
import socket
import time;

channel_id = "1204647940140826694";
bot_token = "MTIwNTAzMzU4OTkzNTQ0NDAzOA.Gqup8l.qqEuzNTwelKZqHUWBYzX1PmgTY10oCVU7IGP6M";


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

if len(bot_token.split("Bot")) > 1:
    bot_token = bot_token.split("Bot ")[len(bot_token.split("Bot ")) - 1];

prev_address = None;

while True:

    time.sleep(5);

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

        baseURL = "https://discord.com/api/channels/" + channel_id + "/messages";
        headers = { "Authorization":"Bot " + bot_token,
                    "Content-Type":"application/json", }

        r = requests.post(baseURL, headers = headers, json={"content":address})
        prev_address = address;
