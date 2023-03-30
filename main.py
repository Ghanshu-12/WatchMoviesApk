from kivy.lang.builder import Builder
from kivymd.app import MDApp
import webbrowser
class WatchMovies(MDApp):
    def watch(self,url):
        webbrowser.open(url)
    def build(self):
        return Builder.load_file('select.kv')
root=WatchMovies()
root.run()