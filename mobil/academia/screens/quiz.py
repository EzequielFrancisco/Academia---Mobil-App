from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.app import App


class QuizScreen(Screen):
    dialog = None

    def on_enter(self, *args):
        if hasattr(self, "_started"):
            return
        self._started = True

        app = App.get_running_app()
        self.questions = app.bd.get_game("history")

        if not self.questions:
            self.ids.label_quiz_question.text = "Sem perguntas disponíveis."
            return

        self.current = 0
        self.load_question()

    def load_question(self):
        container = self.ids.containers_quiz_card
        container.clear_widgets()

        _, _, question, options, _ = self.questions[self.current]
        self.ids.label_quiz_question.text = question

        for index, text in enumerate(options.split("|"), start=1):
            card = MDCard(
                radius=10,
                size_hint=(1, None),
                height=dp(80),
                md_bg_color=(0.9, 0.9, 0.9, 1),
            )

            label = Label(
                text=text,
                color=(0, 0, 0, 1),
                halign="center",
                valign="middle",
            )
            label.bind(size=label.setter("text_size"))

            card.add_widget(label)
            card.bind(on_release=lambda x, i=index: self.check_answer(i))
            container.add_widget(card)

    def check_answer(self, selected):
        correct = self.questions[self.current][4]

        self.show_dialog("Correcto" if selected == correct else "Errado")

        self.current += 1
        if self.current >= len(self.questions):
            self.end_quiz()
        else:
            self.load_question()

    def end_quiz(self):
        self.ids.label_quiz_question.text = "Quiz terminado!"
        self.ids.containers_quiz_card.clear_widgets()

    def show_dialog(self, message):
        if self.dialog:
            self.dialog.dismiss()

        self.dialog = MDDialog(
            title="Resultado",
            text=message,
            size_hint=(0.8, None),
        )
        self.dialog.open()

    def go_home(self):
        self.manager.current = "home"
