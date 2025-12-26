import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from database.db import Database
from kivy.core.window import Window
#import screens
from screens.splash import SplashScreen
from screens.info_splash import InfoSplashScreen
from screens.home import HomeScreen
from screens.quiz import QuizScreen
from screens.form import FormScreen
from screens.memory import MemoryScreen

from kivy.metrics import dp
# sete the winow size (for desktop testing)
Window.size = (360, 640)

class AcademiaApp(MDApp):
    def build(self):
        self.bd = Database()
        self.asset_path = os.path.join(os.path.dirname(__file__), "assets")
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "500"

        return Builder.load_file('screen.kv')

if __name__ == "__main__":
    AcademiaApp().run()
