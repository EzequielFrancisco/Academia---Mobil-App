from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class InfoSplashScreen(Screen):

    def setup(self, info_text, next_screen):
        self.ids.info_label.text = info_text
        self.next_screen = next_screen
        self.ids.progress_bar.value = 0

    def on_enter(self):
        Clock.schedule_interval(self.update_progress, 0.1)

    def update_progress(self, dt):
        bar = self.ids.progress_bar
        if bar.value < 100:
            bar.value += 2
        else:
            Clock.unschedule(self.update_progress)
            self.manager.current = self.next_screen
