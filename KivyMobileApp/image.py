from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MyImageApp(App):
    def build(self):
        img = AsyncImage(source="https://meme-api.com/gimme")
        return img
    
MyImageApp().run()