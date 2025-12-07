import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from database.db import Database
from kivy.core.window import Window
#import screens
from screens.splash import SplashScreen
from screens.home import HomeScreen
from screens.quiz import QuizScreen
from screens.form import FormScreen

# sete the winow size (for desktop testing)
Window.size = (360, 640)

class AcademiaApp(MDApp):
    def build(self):
        self.bd = Database()
        self.asset_path = os.path.join(os.path.dirname(__file__), "assets")
        return Builder.load_file('screen.kv')

if __name__ == "__main__":
    AcademiaApp().run()
