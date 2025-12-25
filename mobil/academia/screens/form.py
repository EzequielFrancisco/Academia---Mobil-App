from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
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

        container = self.ids.form_screen
        fields = container.children[::-1]

        options = [f.text for f in fields]

        app.bd.insert_game(module="math",question=question,options=options,correct=correct)

    def go_home(self):
        self.manager.current = "home"
