import random
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock

class MemoryScreen(Screen):


    def on_enter(self, *args):
        if not hasattr(self, "cards_created"):
            self.sequencia = [
                '7','1','8','2','8','1','8','2','8','4',
                '5','9','0','4','5','2','3','5','3','6',
                '0','2','8','7','4','7','1','3','5','2',
                '6','6','2','4','9','7','7','5','7','2',
                '4','7','0','9','3','6','9','9','9','5',
                '9','5','7','4','9','6','6','9','6','7',
                '6','2','7','7','2','4','0','7','6','6',
                '3','0','3','5','3','5','4','7','5','9',
                '4','5','7','1','3','8','2','1','7','8',
                '5','2','5','1','6','6','4','2','7','4'
            ]
            self.indice_actual = 0  # próximo número esperado
            self.create_cards()
            self.cards_created = True  # garante que a lógica só executa uma vez

    def correct_number(self, number):
        esperado = self.sequencia[self.indice_actual]
        '''Nota: 
            trabalho na logica de verificação aqui, o problema e retirar o numero coreto da sequencia sempre 
            ou seja a cada acerto elima o nuero mas isso esta a dar-me uma dor de cabeça tremenda, pois preciso saber qual o proximo numero em uma ordem seqncial apois verificar eliminar para nao ser mais contado e renciar o jogo.
            para quem mexer aqui boa sorte kkkkkk, e lembre-se de testar bastante. 
        '''
        if number == esperado:
            self.on_notification(f"Correcto: {number}")
            self.indice_actual += 1

            if self.indice_actual >= len(self.sequencia):
                self.on_notification("Parabéns! Concluiu a sequência.")
                self.restart_game()
            else:
                self.create_cards()
        else:
            self.on_notification(f"Errado: {number}")
            self.restart_game()

    def create_cards(self):
        container = self.ids.containers_memory_card
        container.clear_widgets()

        proximo = self.sequencia[self.indice_actual]  # número que deve aparecer

        # pegar outros números aleatórios, sem incluir o próximo
        restantes = [d for d in self.sequencia if d != proximo]
        digitos_aleatorios = random.sample(restantes, min(15, len(restantes)))

        # adiciona o próximo número correto
        digitos = digitos_aleatorios + [proximo]

        # embaralha os 16 números
        random.shuffle(digitos)

        for digito in digitos:
            card = MDCard(
                size_hint=(None, None),
                size=("70dp", "70dp"),
                md_bg_color=(0.4627, 0.2196, 0.9804, 1),
                radius=[10, 10, 10, 10],
                ripple_behavior=True,
                padding="10dp",
            )

            label = MDLabel(
                text=digito,
                halign="center",
                font_style="H5",
                bold=True,
            )

            card.add_widget(label)

            card.bind(
                on_release=lambda x, n=digito: self.correct_number(n)
            )

            container.add_widget(card)

    def on_notification(self, message):
        self.ids.memory_label.text = message

    def restart_game(self):
        self.indice_actual = 0
        self.create_cards()

    def life_cycle(self):
        pass

    def go_home(self):
        self.manager.current = "home"