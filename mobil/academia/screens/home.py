from logging import info
from sys import modules
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.app import App
class HomeScreen(Screen):

    def screen_root(self, screen):
        match screen:
            case "quiz":
                self.manager.current = "quiz"
            case "inglês":
                self.manager.current = "inglês"
            case "historia":
                info = """Aprenda errando factos historicos sobre Angola e Africa"""
                self.manager.get_screen("info_splash").setup(info_text=info, next_screen="quiz")
                self.manager.current = "info_splash"
            case "memoria":
                # self.manager.current = "memory"
                info = """Euler é (2.71828...) a base do logaritmo natural.\nO objectivo deste jogo é encontrar os dígitos correspondentes.\nNo menor número de tentativas possível\n\ne=2,7182818284 5904523536 0287471352 6624977572 4709369995 9574966967 6277240766 3035354759 4571382178 5251664274."""
                self.manager.get_screen("info_splash").setup(info_text=info, next_screen="memory")
                self.manager.current = "info_splash"
            
    def create_modules(self):
        # Criar o layout com o campo de texto
        box = MDBoxLayout(
            orientation="vertical",
            padding="10dp",
            spacing="10dp"
        )
        text_field = MDTextField(hint_text="Insira o nome do seu módulo")
        box.add_widget(text_field)

        # Função que será chamada ao clicar no OK
        def on_ok(instance):
            nome_modulo = text_field.text  # pega o valor do campo
            app = App.get_running_app()
            app.bd.insert_module(nome_modulo)  
            self.dialog.dismiss()

        # Criar o diálogo
        self.dialog = MDDialog(
            title="",
            type="custom",
            content_cls=box,
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=(0,0,0,1),
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=(0,0,0,1),
                    on_release=on_ok  # aqui liga a função
                ),
            ]
        )

        self.dialog.open()


    def on_enter(self, *args):
        # Troca de slide a cada 3 segundos
        Clock.schedule_interval(self.next_slide, 3)
        self.render_modules()
        

    def next_slide(self, dt):
        carousel = self.ids.carousel  # aqui self.ids, não self.root.ids
        carousel.load_next(mode='next') 
    
    
    def render_modules(self):
        app = App.get_running_app()
        modules = app.bd.get_modules()  # lista de módulos do BD

        container = self.ids.modulos_home_card
        # container.clear_widgets()

        for module in modules:
            module_name = module[1]  # assumindo que module[1] é o nome do módulo
            # Cria o card
            card = MDCard(
                size_hint=(None, None),
                size=("90dp", "90dp"),
                radius=[20, 20, 20, 20],
                md_bg_color=(0.4627, 0.2196, 0.9804, 1),
                ripple_behavior=True,
            )

            # Layout interno vertical
            box = MDBoxLayout(
                orientation="vertical",
                spacing="8dp",
                size_hint=(1, 1),
                padding="10dp"
            )

            # Label centralizado com o nome do módulo
            label = MDLabel(
                text=module_name,  # assumindo que module é uma string com o nome
                halign="center",
                font_style="Button",
                bold=True
            )

            box.add_widget(label)
            card.add_widget(box)

            # Se quiser ação ao clicar no card
            card.on_release = lambda m=module: self.screen_root(m)

            # Adiciona o card no container
            container.add_widget(card)
        
    
    

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
