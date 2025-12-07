from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.label import Label
from kivy.metrics import dp

class HomeScreen(Screen):

    def screen_root(self, screen):
        match screen:
            case "quiz":
                print("quiz screen")
    
    def on_enter(self, *args):
        # Só cria o carrossel a primeira vez!
        # if not self.ids.carousel.children:
            # self.create_carousel()
        pass
'''
    def create_carousel(self):
        carousel = self.ids.carousel
        carousel.clear_widgets()

        for i in range(5):

            slide = MDBoxLayout(
                orientation="vertical",
                size_hint=(None, None),
                width=dp(600),
                height=dp(200),
                pos_hint={"center_x": 0.5},
                spacing=dp(1),
            )

            inner = MDBoxLayout(
                orientation="vertical",
                size_hint=(0.9, 1),
                md_bg_color=(0.2, 0.5, 0.9, 1),
                radius=[20, 20, 20, 20],
                padding=dp(1),
                spacing=dp(1),
            )

            btn = MDFillRoundFlatButton(text=f"Quiz {i+1}")
            btn.bind(on_release=lambda a, idx=i: self.screen_root("quiz"))

            lbl = Label(
                text=f"Quiz {i+1}",
                color=(1, 1, 1, 1),
                font_size="22sp",
                halign="center"
            )

            inner.add_widget(btn)
            inner.add_widget(lbl)

            slide.add_widget(inner)

            carousel.add_widget(slide)
    '''
