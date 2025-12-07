from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField

class FormScreen(Screen):
    def create_question(self, cont):
        container = self.ids.form_screen

        for i in range(cont):
            field = MDTextField(
                hint_text=f"resposta {i}",
                pos_hint={"center_y": 0.5},
                #size_hint_x=0.8,
                #size_hint_y=0.1,
            )
            container.add_widget(field)
