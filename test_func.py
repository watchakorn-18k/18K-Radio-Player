

# from pypresence import Presence
# rpc = Presence(835456436393738240)
# rpc.connect()
# rpc.update(state="test", details="test details", large_image="18k-radio", large_text="18K Radio", small_image="play", small_text="play")
# from time import sleep~
from vlc import EventType, Media, MediaPlayer, MediaParseFlag, Meta

def _media_cb(event, *unused):
    # XXX callback ... never called
    print(event)

p = MediaPlayer()
# cmd1 = "sout=file/ts:%s" % outfile
media = Media("http://112.121.151.133:8147/live")  # , cmd1)
# media.get_mrl()
p.set_media(media)
p.play()

e = p.event_manager()
e.event_attach(EventType.MediaMetaChanged, _media_cb, media)
e.event_attach(EventType.MediaParsedChanged, _media_cb, media)


meta = {Meta.Album: None,
        Meta.Genre: None,
        Meta.NowPlaying: None,
        Meta.Title: None,
        Meta.ShowName: None,}


print(media.get_meta(Meta.Album),media.get_meta(Meta.Genre),media.get_meta(Meta.NowPlaying))

while True:  # loop forever
    # XXX using MediaParseFlag.local is not any different
    media.parse_with_options(MediaParseFlag.network, 2)  # 2 sec timeout
    # XXX media.get_parsed_status() always returns .skipped
    for k in meta.keys():
        v = media.get_meta(k)
        print(v)
        print(k)
        print(meta.keys())
        if v != meta[k]:
            print(v)
            print("{} - {}".format(k, v))
            meta[k] = v
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
