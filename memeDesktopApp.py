from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import mainthread
import requests

class MyImageApp(App):
    def build(self):
        self.img = AsyncImage()
        self.fetch_image_url()
        layout = BoxLayout(orientation='vertical')
        refresh_button = Button(text='Next Image',size_hint=(0.5,0.15), pos_hint={"center_x":0.5,"center_y":0.15}, font_size="12sp")
        refresh_button.bind(on_release=self.refresh_image)
        layout.add_widget(self.img)
        layout.add_widget(refresh_button)
        return layout

    def fetch_image_url(self):
        url = "https://meme-api.com/gimme"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            image_url = data['url']
            self.update_image(image_url)
        else:
            print("Failed to fetch image URL")

    @mainthread
    def update_image(self, url):
        self.img.source = url

    def refresh_image(self, instance):
        self.fetch_image_url()

if __name__ == '__main__':
    MyImageApp().run()
