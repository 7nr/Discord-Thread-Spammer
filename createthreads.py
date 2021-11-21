try:
    import requests, time, os
except:
    os.system("pip install requests")
    import requests
    import time
    import os

token = str(input(" ~ Enter Token: "))
channel_id = str(input(" ~ Enter Channel ID: "))
thread_name = str(input(" ~ Enter Thread name: "))
header = {"content-type": "application/json",
            "Authorization": token}
while True:    
    r = requests.post(f"https://canary.discord.com/api/v9/channels/{channel_id}/threads", headers=header, json={
                    "name": thread_name, "type": 11, "auto_archive_duration": 60})
    if r.status_code == 200 or r.status_code == 201:
        print(f" > Created thread -> ID: {r.json()['id']}")
    elif r.status_code == 429:
        print(f" ! Ratelimited - Delaying {r.json()['retry_after']}s")
        time.sleep(int(r.json()['retry_after']))
    else:
        print(" ! Weird Error join for help -> https://discord.gg/kPjY7HTbJJ")
