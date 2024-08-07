from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App


KV = """
<EndScreen>:
    name: 'end'
    MDLabel:
        text: "thank you for scouting by doing so you help the team be better in the next game" 
        text_color: [1,1,1,1]
        pos_hint: {'center_x': 0.5,'center_y': 0.6}
        halign: "center"
        font_size: "30sp"
        padding: 20
    MDRectangleFlatButton:
        text: 'exit'
        text_color: [0, 0, 0, 1]
        md_bg_color: [1, 0, 1, 1]
        pos_hint: {'center_x': 0.5, 'center_y': 0.07}
        on_press: 
            root.exit()

    
"""


Builder.load_string(KV)

class EndScreen(Screen):
    def exit(self):
        App.get_running_app().stop()