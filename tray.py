


from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk


def show_window():
    icon.stop()
def quit_window():
    icon.stop()


image = Image.open("logo_title.ico")
menu = (item('Quit', quit_window), item('Show', show_window))
icon = pystray.Icon("name", image, "title", menu)
icon.run()

# window = tk.Tk()
# window.title("Welcome")

# def quit_window(icon, item):
#     icon.stop()
#     window.destroy()

# def show_window(icon, item):
#     icon.stop()
#     window.after(0,window.deiconify)

# def withdraw_window():  
#     window.withdraw()
#     image = Image.open("logo_title.ico")
#     menu = (item('Quit', quit_window), item('Show', show_window))
#     icon = pystray.Icon("name", image, "title", menu)
#     icon.run()

# if __name__ == '__main__':
#     withdraw_window()
#     window.mainloop()

# class Tray():
#     from infi.systray import SysTrayIcon
#     def __init__(self):
#         self.hover_text = "18K"
#         self.menu_options = (('Say Hello', "Logo.png", self.hello),
#                     ('Do nothing', None, self.do_nothing),
#                     ('A sub-menu', "Logo.png", (('Say Hello to Simon', "Logo.png", self.simon),
#                                                 ('Do nothing', None, self.do_nothing),
#                                                 ))
#                 )
#         self.sysTrayIcon = self.SysTrayIcon("main.ico", self.hover_text, self.menu_options, default_menu_index=1)
         
#     def hello(self, *args):
#         print("Hello World")
#         Window.show()
#     def simon(self, *args):
#         print("Hello Simon")
        
#     def bye(self, *args):
#         print('Bye, then.') 
#         self.sysTrayIcon.shutdown()
#     def do_nothing(self, *args):
#         pass
#     def start_up(self, *args):
#         self.sysTrayIcon.start()