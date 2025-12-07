from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.app import App


class QuizScreen(Screen):
    dialog = None

    def on_enter(self, *args):
        self.create_game()

    def select_card(self, card_id):
        self.show_dialog()

    def create_game(self):
        app = App.get_running_app()   # ← CORREÇÕES AQUI
        data = app.bd.get_game()

        print(data)

        container = self.ids.containers_quiz_card

        options = MDCard(
            radius=10,
            size_hint=(1, None),
            height=dp(80),
            md_bg_color=(0.9, 0.9, 0.9, 1)
        )

        label = Label(
            text="Luanda",
            color=(0, 0, 0, 1),
            halign="center",
            valign="middle"
        )
        label.bind(size=label.setter("text_size"))

        options.add_widget(label)
        container.add_widget(options)

    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Sucesso",
                text="Correcto",
                size_hint=(0.8, None)
            )
        self.dialog.open()
