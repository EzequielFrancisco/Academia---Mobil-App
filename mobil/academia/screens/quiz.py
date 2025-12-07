from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog

class QuizScreen(Screen):
    dialog = None

    def select_card(self, card_id):
        pergunta = "Capital de Angola"
        resposta_escolhida = card_id

        # guardar no BD
        app = self.manager.app
        app.bd.adicionar_resposta(pergunta, resposta_escolhida, 1 if card_id == "card6" else 0)

        if card_id == "card6":
            self.show_dialog()

    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Sucesso",
                text="Correcto",
                size_hint=(0.8, None)
            )
        self.dialog.open()
