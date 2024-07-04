from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import Screen
# Your KV string
KV = """
<TeleopEndGamePeriod>:
    name: 'end'
    MDLabel:
        text: "click on what append in the game"
        pos_hint: {'center_x': 0.5,'center_y': 0.9}
        halign: "center"
        font_size: "17sp"
"""

Builder.load_string(KV)

class TeleopEndGamePeriod(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget()
    def create_widgets(self):
        texts = [
            "Didn't try to climb",
            "tried to climb but failed",
            "climb alone",
            "climb in harmony",
            "trap alone",
            "trap in harmony",
        ]

        y_level = [0.8, 0.67, 0.54, 0.41, 0.28, 0.15]

        for i, text in enumerate(texts):
            box = MDBoxLayout(
                pos_hint={'center_x': 0.5, 'center_y': y_level[i]},
                size_hint=(0.9, None),
                size=[0, 70],
                size_hint_min_y=None,
                md_bg_color=(1, 0, 0, 1),
                radius=[5]
            )
            label = MDLabel(
                text=text,
                halign='center',
                font_size="25sp",
                pos_hint={'center_x': 0.7, 'center_y': 0.5},
                color=(1, 1, 1, 1)
            )
            box.add_widget(label)
            self.add_widget(box)

        for y in y_level:
            button = MDRectangleFlatButton(
                md_bg_color=(0, 0, 0, 0),
                text="",
                size_hint=(0.9, None),
                size=[0, 70],
                pos_hint={'center_x': 0.5, 'center_y': y}
            )
            self.add_widget(button)