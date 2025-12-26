from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.app import App


class FormScreen(Screen):

    def create_quiz(self, cont):
        container = self.ids.form_screen

        for _ in range(cont):
            field = MDTextField(
                hint_text=f"Resposta {len(container.children) + 1}",
                size_hint_x=0.9,
                pos_hint={"center_x": 0.5},
                mode="rectangle",
            )
            container.add_widget(field)

    def submit_quiz(self):
        app = App.get_running_app()

        question = self.ids.question.text
        correct = self.ids.correct.text
        modulo = self.ids.btn_opcao.text

        container = self.ids.form_screen
        fields = container.children[::-1]

        options = [f.text for f in fields]
        if not question or not correct or len(options) < 2:
            self.show_alert_dialog("Por favor, preencha todos os campos corretamente.")
            return
        try:
            app.bd.insert_game(
                module=modulo,
                question=question,
                options=options,
                correct=correct
            )   
        except Exception as e:
            self.show_alert_dialog(f"Erro ao salvar o quiz: {e}")
            return
            
        self.show_alert_dialog("Quiz salvo com sucesso!")
        self.reset_form()
        
    def show_alert_dialog(self, message):

        self.dialog = MDDialog(
            text=message,
            buttons=[
                MDFlatButton(
                    text="Ok",
                    theme_text_color="Custom",
                    text_color = (0, 0.5, 1, 1),
                    on_release=lambda x: self.dialog.dismiss(),
                ),
            ],
        )
        self.dialog.open()

    def reset_form(self):
        # Limpa os campos fixos
        self.ids.question.text = ""
        self.ids.correct.text = ""

        # Remove todos os campos de resposta
        container = self.ids.form_screen
        container.clear_widgets()

    def go_home(self):
        self.manager.current = "home"
    
    def menu_modulos(self):
        itens = [
            {
                "text": "math",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="math": self.selecionar_modulo(x)
            },
            {
                "text": "history",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="history": self.selecionar_modulo(x)
            },
        ]

        self.menu = MDDropdownMenu(
            caller=self.ids.btn_opcao,
            items=itens,
            width_mult=4,
        )
        self.menu.open()

    def selecionar_modulo(self, texto):
        self.ids.btn_opcao.text = texto  # atualiza o botão
        self.menu.dismiss()              # fecha o menu

