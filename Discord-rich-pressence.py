import rpc
import time
from time import mktime

print("Demo for python-discord-rpc Adobe illustrator")
client_id = '835456436393738240'  # Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "18K-STATION",  # anything you like
            "details": "18K-STATION",  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "เล่น",  # anything you like
                "small_image": "play",  # must match the image key
                "large_text": "18K-RADIO",  # anything you like
                "large_image": "18k-radio"  # must match the image key
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(900)
