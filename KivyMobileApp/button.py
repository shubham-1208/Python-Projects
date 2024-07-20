from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)

class BadBoyApp(App):
    def build(self):
        # label = Label(text = "Hello World", font_size="120sp", bold=True, italic=True,color=(1,0,0,1))
        btn = Button(text="click me", size_hint=(0.25,0.15), pos_hint={"center_x":0.15,"center_y":0.15}, font_size="12sp", on_press=self.btn_click)
        return btn
    def btn_click(self, btn):
        print("btn clicked")
        label = Label(text = "Hello World", font_size="120sp", bold=True, italic=True,color=(1,0,0,1))
        return label
BadBoyApp().run()