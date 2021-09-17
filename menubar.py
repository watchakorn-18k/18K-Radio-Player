from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

kv_string = '''
<MyWidget>:
    Label:
        height: '60dp'
        background_color: '#1d1719'
        canvas:
            Color:
                rgb: 0.1, 0.6, 0.3
            Rectangle:
                size: self.size     
                pos: self.pos
            Clear
            Color:
                rgb: 0.6, 0.2, 0.1
            Rectangle:
                size: self.size     
                pos: self.pos
'''

Builder.load_string(kv_string)

class MyWidget(Widget):
    pass

class TestApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    TestApp().run()