from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.set('kivy','window_icon','Logo.png')
Config.set('kivy','default_font',['Kanit', 'fonts/Kanit-Regular.ttf'])
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window
import vlc
from vlc import EventType, Media, MediaPlayer, MediaParseFlag, Meta
from kivy.clock import Clock
import threading
import random
from pypresence import Presence
import rpc
import time
from time import mktime

try:
    client_id = '835456436393738240'  # Your application's client ID as a string. (This isn't a real client ID)
    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
except:
    pass


# def play_music_pre():
#     media.audio_set_volume(0)
#     while True:
#         media_link.parse_with_options(MediaParseFlag.network, 2)
#         meta_name = media_link.get_meta(Meta.NowPlaying)
#         meta_18K = media_link.get_meta(Meta.Genre)
#         meta_Title = media_link.get_meta(Meta.Title)
#         if meta_name != None:
#             meta = []
#             meta.append(meta_name)
#             meta.append(meta_18K)
#             meta.append(meta_Title)
#             return meta
#             break
#         elif meta_name == None:
#             threading.Thread(target=media.play()).start()
#             print(meta_name)  

media = MediaPlayer()
media_link = Media("http://112.121.151.133:8147/live")
media.set_media(media_link)
# title_name_music = media_link.get_meta(Meta.NowPlaying)
# title_name_music = play_music_pre()
# title_name_music = title_name_music[0]
# radio_name = play_music_pre()
# radio_name = radio_name[1]
# dj_name = play_music_pre()
# dj_name = dj_name[2]
# print(radio_name,dj_name)
radio_name = "สถานีความคิด"
title_name_music = radio_name
dj_name = "ของทุกชีวิต ที่มีความทุกข์"
time_start = time.time()
time_start = int(time_start)

# rpc.update(
#   large_image="18k-radio",
#   small_image="play",
#   buttons=[{"label": f"{title_name_music[0:29]}",
#    "url": "https://ecq-studio.com/18K/X/"},
#    {"label": f"{dj_name}",
#     "url": "https://ecq-studio.com/18K/X/"}],)
def activity_start(song,dj,status_song):
    activity = {
            "state": f"{song}",
            "details": f"{dj}",  # anything you like
            "timestamps": {
                "start": time_start
            },
            "assets": {
                "small_text": "เล่น",  # anything you like
                "small_image": f"{status_song}",  # must match the image key
                "large_text": "18K-RADIO",  # anything you like
                "large_image": "18k-radio"  # must match the image key
            }
        }
    return activity
rpc_obj.set_activity(activity_start(dj_name,title_name_music,"play"))

class Radio_Player(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        

class Bottom_layout(BoxLayout):

      
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radio_name = str(radio_name)
        self.dj_name = str(dj_name)
        
        for i in range(0,2):
            self.add_widget(Label(text=f''))
        
        
        
    
    def volume(self,widget):
        volume_from_slider = int(widget.value)
        media.audio_set_volume(volume_from_slider)
        print("vol",volume_from_slider)
        return volume_from_slider
    
    def on_state_mute_unmute(self,widget):
        if widget.state == 'normal':
            self.ids.img_sound.source = 'unmute.png' 
            print("เปิดเสียง")
            media.audio_set_volume(int(self.ids.slider.value)) 
            print(int(self.ids.slider.value))
            # self.ids.name_song.text = title_name_music
            self.ids.name_song.text = "เปิดเสียง"
            Clock.schedule_once(self.title_name_callback, 2)
        elif widget.state == 'down':
            self.ids.img_sound.source = 'mute.png'
            print("ปิดเสียง")
            media.audio_set_volume(0)
            self.ids.name_song.text = "ปิดเสียง"
            Clock.schedule_once(self.title_name_callback, 2)
            print(media.audio_set_volume(0))
    def on_state_play_pause(self,widget):
        if widget.state == 'normal':
            self.ids.img_player.source = 'play.png' 
            print('หยุดเล่น',int(self.ids.slider.value))
            media.pause()
            self.time_start = time.time()
            self.status_media = "pause"
            rpc_obj.set_activity(activity_start(dj_name,title_name_music,self.status_media))
            try: 
                threading.Thread(target=self.cancel_update_name_title(self.event)).start()
            except AttributeError:
                print("error")
            self.ids.name_song.text = self.radio_name
        elif widget.state == 'down':
            self.time_start = time_start
            self.status_media = 'play'
            self.ids.name_dj.text  = dj_name
            # rpc.update(state=f"{self.ids.name_dj.text}", details=f"{self.ids.name_song.text}", large_image="18k-radio",small_image=self.status_media,buttons=[{"label": f"{title_name_music[0:29]}", "url": "https://ecq-studio.com/18K/X/"},{"label": f"{self.ids.name_dj.text}", "url": "https://ecq-studio.com/18K/X/"}],start=self.time_start,party_id="Md10sAsisda101sxs")
            self.ids.img_player.source = 'pause.png'
            print('เล่น',int(self.ids.slider.value))
            run_t = threading.Thread(target=self.update_name_title).start()
            rpc_obj.set_activity(activity_start(self.ids.name_dj.text,self.ids.name_song.text,self.status_media))
            print("ก่อน",self.ids.mute_volume.state,self.ids.play_pause.state)
            if self.ids.mute_volume.state == 'down' and self.ids.play_pause.state == 'down':
                print(self.ids.mute_volume.state,"ปิดทั้งคู่")
                media.audio_set_volume(0)
                media.play()
            elif self.ids.mute_volume.state == 'normal':
                print(self.ids.mute_volume.state)
                media.audio_set_volume(int(self.ids.slider.value))
                media.play()
            else:
                print("อื่นๆ")
                media.audio_set_volume(0)
                media.play()

                
            
    def loop_name_title(self,*args):
        title_name_music = media_link.get_meta(Meta.NowPlaying)
        dj_name = media_link.get_meta(Meta.Title)
        self.ids.name_song.text = title_name_music[0:40]+" ฯลฯ"
        self.ids.name_dj.text = dj_name
        # rpc.update(state=f"{self.ids.name_dj.text}", details=f"{self.ids.name_song.text}", large_image="18k-radio",small_image=self.status_media,buttons=[{"label": f"{self.ids.name_song.text[0:32]}", "url": "https://ecq-studio.com/18K/X/"},{"label": f"{self.ids.name_dj.text}", "url": "https://ecq-studio.com/18K/X/"}],start=time_start)
        print(title_name_music,dj_name)
        detial_song = [dj_name,title_name_music]
        rpc_obj.set_activity(activity_start(self.ids.name_dj.text,self.ids.name_song.text,self.status_media))
    
    def update_name_title(self,*args):
        self.event = Clock.schedule_interval(self.loop_name_title,5)
        return self.event
    def cancel_update_name_title(self,*args):
        rpc.update(state=f"{self.ids.name_dj.text}", details=f"{self.ids.name_song.text}", large_image="18k-radio",small_image=self.status_media,buttons=[{"label": f"{title_name_music[0:29]}", "url": "https://ecq-studio.com/18K/X/"},{"label": f"{self.ids.name_dj.text}", "url": "https://ecq-studio.com/18K/X/"}],start=time_start)
        self.delete_update = Clock.unschedule(self.event)
    def title_name_callback(self,*args):
        self.ids.name_song.text = title_name_music
           
class RadioApp(App):
        
        def build(self): 
            
            self.title = "18K Radio | สถานีความคิด ของทุกชีวิต ที่มีความทุกข์"
            self.title_color = 1,0,0,1
            self.icon = 'Logo.png'
            # Window.borderless = '1'
            return Radio_Player()


if __name__ == "__main__":
    RadioApp().run()
    

