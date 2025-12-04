from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog

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


class HomeScreen(Screen):
    pass


class AcademiaApp(MDApp):
    def build(self):
        return Builder.load_file('screen.kv')
    
    def select_card(self, card_id):
        live = 3
        print(f"Card {card_id} selected")

        if card_id == "card6":
            self.show_dialog()
        else:
            live -= 1
            
    
    def show_dialog(self):
        dialog = MDDialog(title="Sucesso", text="Correcto", size_hint=(0.8, None), height=200)
        dialog.open()


if __name__ == "__main__":
    AcademiaApp().run()
