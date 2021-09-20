from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
# Config.set('graphics', 'borderless', '1')
Config.set('graphics', 'multisamples', '0')
Config.set('kivy','window_icon','Logo.png')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('kivy','default_font',['Kanit', 'fonts/Kanit-Regular.ttf'])


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock



import json
import requests
from vlc import Media, MediaPlayer, Meta
from threading import Thread
from multiprocessing.pool import ThreadPool
import rpc
import time
from pystray import MenuItem as item
import pystray
from PIL import Image
import os
import asyncio




pool = ThreadPool(processes=5)

# client_id = '835456436393738240'  # Your application's client ID as a string. (This isn't a real client ID)
# rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module


# def loop_upload():
#     try:
#         url_update = requests.get('https://web-18k-mongodb-crud.herokuapp.com/api/get_18k_list_dj')
#     except: 
#         pass
#     print("update json",url_update)
#     data = url_update.json()
#     with open('dj.json', 'w') as f:
#         json.dump(data, f)

# try:
    
#     rpc.connect()
# except:
#     pass

# def radio_link():
#     media_link = Media("http://112.121.151.133:8147/live")
#     return media_link

# def radio_server(media_link):
#     media = MediaPlayer()
#     media_link = media_link
#     media.set_media(media_link)
#     return media
    
radio_name = "สถานีความคิด"
title_name_music = radio_name
dj_name = "ของทุกชีวิต ที่มีความทุกข์"
# time_start = time.time()
# time_start = int(time_start)

# def activity_start(song,dj,status_song):
#     button = [{"label": f"{dj[0:29]}",
#    "url": "https://ecq-studio.com/18K/X/"},
#    {"label": f"{song}",
#     "url": "https://ecq-studio.com/18K/X/"}]
#     activity = {
#             "state": f"{song}",
#             "details": f"{dj}",  # anything you like
#             "timestamps": {
#                 "start": time_start
#             },
#             "assets": {
#                 "small_text": "เล่น",  # anything you like
#                 "small_image": f"{status_song}",  # must match the image key
#                 "large_text": "18K-RADIO",  # anything you like
#                 "large_image": "18k-radio"  # must match the image key
#             }
#         }
#     return activity
    
# rpc_obj.set_activity(activity_start(dj_name,title_name_music,"play"))



class Radio_Player(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     self.img_dj = str('LOGO18K.png')
    #     super().__init__(**kwargs)
    #     # self.media_link = radio_link()
    #     # self.media = radio_server(self.media_link)
    #     # self.media.audio_set_volume(0)
    #     # self.media.play()
    #     # Clock.schedule_interval(self.update_dj,1)

    # def loop_name_title(self,*args):
    #     try:
    #         self.title_name_music = self.media_link.get_meta(Meta.NowPlaying)
    #         self.dj_name = self.media_link.get_meta(Meta.Title)
    #     except:
    #         pass
    #     return self.dj_name
    #     print(self.img_dj)

    # def update_dj(self,*args):
    #     from dj import Dj
    #     from img_dj import img_Dj
    #     import time
    #     start_time = time.time()
    #     dj = Dj.get_dj()
    #     img_dj = img_Dj.get_dj()
    #     d = {}
    #     for i in range(len(dj)):
    #         d[f"{dj[i]}".format(i)] = img_dj[i]
    #     print(d["DJ PORTON007"])
    #     try:
    #         self.img_dj = self.loop_name_title()
    #         self.ids.img_djs.source = f'{d[self.img_dj]}'
    #     except:
    #         pass
    #     print("--- %s seconds ---" % (time.time() - start_time))
    # def loop_name_title(self,*args):
    #     try:
    #         self.title_name_music = self.media_link.get_meta(Meta.NowPlaying)
    #         self.dj_name = self.media_link.get_meta(Meta.Title)
    #     except:
    #         pass
    #     return self.dj_name
        
        
        
class Bottom_layout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
        self.radio_name = str(radio_name)
        self.dj_name = str(dj_name)
        self.detail = []
        self.add_widget(Label(text=f''))
    #     # try:
    #     #     self.media_link = radio_link()
    #     #     self.media = radio_server(self.media_link)
    #     # except :
    #     #     pass
    
    # def volume(self,widget):
    #     volume_from_slider = int(widget.value)
    #     self.media.audio_set_volume(volume_from_slider)
    #     print("vol",volume_from_slider)
    #     return volume_from_slider
    
    # def on_state_mute_unmute(self,widget):
    #     if widget.state == 'normal':
    #         self.ids.img_sound.source = 'unmute.png' 
    #         print("เปิดเสียง")
    #         # self.media.audio_set_volume(int(self.ids.slider.value)) 
    #         # print(int(self.ids.slider.value))
    #         # self.ids.name_song.text = title_name_music
    #         self.ids.name_song.text = "เปิดเสียง"
    #         # Clock.schedule_once(self.title_name_callback, 2)

    #     elif widget.state == 'down':
    #         self.ids.img_sound.source = 'mute.png'
    #         # self.media.audio_set_volume(0)
    #         # self.ids.name_song.text = "ปิดเสียง"
    #         # # Clock.schedule_once(self.title_name_callback, 2)
    #         # print(self.media.audio_set_volume(0))

    # def on_state_play_pause(self,widget):

    #     if widget.state == 'normal':   
    #         try: 
    #             self.ids.img_player.source = 'play.png' 
    #             self.media.pause()
    #             self.status_media = "pause"
    #             rpc_obj.set_activity(activity_start(dj_name,title_name_music,self.status_media))
    #             self.cancel_update_name_title(self.event)
    #         except Exception as e:
    #             print(e)
    #         self.ids.name_song.text = self.radio_name

    #     elif widget.state == 'down':
    #         try:
    #             self.status_media = 'play'
    #             self.ids.name_dj.text  = dj_name
    #             self.ids.img_player.source = 'pause.png'
    #             # thread_update_name_music = pool.apply_async(self.update_name_title)
    #             # thread_update_name_music.get()
                
    #             if self.ids.mute_volume.state == 'down' and self.ids.play_pause.state == 'down':
    #                 self.media.audio_set_volume(0)
    #                 self.media.play()
                    

    #             elif self.ids.mute_volume.state == 'normal':
    #                 self.media.audio_set_volume(int(self.ids.slider.value))
    #                 self.media.play()
                    

    #             else:
    #                 self.media.audio_set_volume(0)
    #                 self.media.play()
                    
    #         except:
    #             pass

    # def loop_name_title(self,*args):
    #     try:
    #         title_name_music = self.media_link.get_meta(Meta.NowPlaying)
    #         dj_name = self.media_link.get_meta(Meta.Title)
    #         self.ids.name_song.text = title_name_music[0:40]+" ฯลฯ"
    #         self.ids.name_dj.text = dj_name
    #         # rpc.update(state=f"{self.ids.name_dj.text}", details=f"{self.ids.name_song.text}", large_image="18k-radio",small_image=self.status_media,buttons=[{"label": f"{self.ids.name_song.text[0:32]}", "url": "https://ecq-studio.com/18K/X/"},{"label": f"{self.ids.name_dj.text}", "url": "https://ecq-studio.com/18K/X/"}],start=time_start)
    #         print(title_name_music,dj_name)
    #         self.detail = [dj_name,title_name_music]
    #         self.update_rpc()
    #     except:
    #         pass
        
    
    # def update_name_title(self,*args):
    #     # self.event = Clock.schedule_interval(self.loop_name_title,5)
        
    #     return self.event
    # def cancel_update_name_title(self,*args):
    #     # self.delete_update = Clock.unschedule(self.event)
    #     pass
    # def title_name_callback(self,*args):
    #     self.ids.name_song.text = title_name_music
    # def update_rpc(self,*args):
    #     print(self.detail)
    #     if self.detail != []:
    #         rpc_obj.set_activity(activity_start(self.detail[0],self.detail[1],self.status_media))

class Menubar(BoxLayout,App):
    def __init__(self, **kwargs):
        self.title_tray = "18K | Player"
        super().__init__(**kwargs)
    def Close_app(self):
        import os
        os._exit(0)
    def Tray(self):
        Window.hide()
    def show_window(self):
        Window.show()
    def quit_window(self):
        import os
        os._exit(0)
        return self.count
    def counts(self,**args):
        self.count += 1
        return self.count
    def tray(self,**args):
        image = Image.open("logo_title.ico")
        menu = (item('เปิดหน้าต่าง',  self.show_window),item('ปิด', self.quit_window))
        icon = pystray.Icon("name", image, self.title_tray, menu)
        self.run = icon.run
        return self.run
   
# Thread(target=Menubar().tray()).start()
# Thread(target=loop_upload()).start()
    
class Status(BoxLayout,App):
    pass


class RadioApp(App):
        # Builder.load_file('testApp.kv')
        def build(self): 
            self.title = "18K Radio | สถานีความคิด ของทุกชีวิต ที่มีความทุกข์"
            self.title_color = 1,0,0,1
            self.icon = 'Logo.png'
            return Radio_Player()


if __name__ == "__main__":
    RadioApp().run()
    

