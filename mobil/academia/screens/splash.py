from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class SplashScreen(Screen):

    def on_enter(self):
        # Change the screen after 2 seconds.
        #Clock.schedule_once(self.go_home, 3)
        Clock.schedule_interval(self.update_progress, 0.1)

    def update_progress(self, dt):
        progress_bar = self.ids.progress_bar
        if progress_bar.value < 100:
            progress_bar.value += 1
        else:
            Clock.unschedule(self.update_progress)
            self.go_home()

    def go_home(self, *args):
        self.manager.current = "home"
        # self.manager.current = "quiz"
