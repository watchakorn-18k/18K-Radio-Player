# from pystray import MenuItem as item
# import pystray
# from PIL import Image
# def close_application(self,):
#     Window.close()
# image = Image.open("LOGO_DISCORD.png")
# menu = (item('ปิด', close_application), item('name', close_application))
# icon = pystray.Icon("name", image, "title", menu)
# icon.run()





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
    
# from vlc import EventType, Media, MediaPlayer, MediaParseFlag, Meta

# def _media_cb(event, *unused):
#     # XXX callback ... never called
#     print(event)

# p = MediaPlayer()
# # cmd1 = "sout=file/ts:%s" % outfile
# media = Media("http://112.121.151.133:8147/live")  # , cmd1)
# # media.get_mrl()
# p.set_media(media)
# p.play()


# e = p.event_manager()
# e.event_attach(EventType.MediaMetaChanged, _media_cb, media)
# e.event_attach(EventType.MediaParsedChanged, _media_cb, media)


# meta = {Meta.Album: None,
#         Meta.Genre: None,
#         Meta.NowPlaying: None,
#         Meta.Title: None,
#         Meta.ShowName: None,}
# print(p.get_length())
# sleep(5)
# print(media.get_meta(Meta.Album),media.get_meta(Meta.Genre),media.get_meta(Meta.NowPlaying))


# while True:  # loop forever
#     # XXX using MediaParseFlag.local is not any different
#     media.parse_with_options(MediaParseFlag.network, 2)  # 2 sec timeout
#     # XXX media.get_parsed_status() always returns .skipped
#     for k in meta.keys():
#         v = media.get_meta(k)
#         print(v)
#         print(k)
#         print(meta.keys())
#         if v != meta[k]:
#             print(v)
#             print("{} - {}".format(k, v))
#             meta[k] = v
#     sleep(2)

# Run = True
# while True:
#     control = int(input("Enter keyword : "))
#     if control == 1:
#         media.play()
#         value = media.get_title()
#         print(value)
#         while Run:
#             control = int(input("Enter keyword : "))
#             if control == 1:
#                 Run = True
#             elif control == 0:
#                 Run = False
#     elif control == 2:
#         media.audio_set_volume(50)
#     elif control == 3:
#         media.audio_set_volume(100)
#     elif control == 0:
#         media.stop()
