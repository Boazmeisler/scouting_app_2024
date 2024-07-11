from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from Variables import DynamicVariables, Constants
from kivy.app import App


KV = """
<TeleopEndGamePeriod>:
    name: 'end'
    MDLabel:
        text: "Click on what happened in the game"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        halign: "center"
        font_size: "17sp"


    MDRectangleFlatButton:
        id: DidntTry
        md_bg_color: 1, 0, 0, 1
        text: "Didn't try to climb"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        on_press:
            root.endGameButtonFunctionality(DidntTry)

    MDRectangleFlatButton:
        id: TriedAndFail
        md_bg_color: 1, 0, 0, 1
        text: "Tried but failed"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.67}
        on_press:
            root.endGameButtonFunctionality(TriedAndFail)

    MDRectangleFlatButton:
        id: ClimbAlone
        md_bg_color: 1, 0, 0, 1
        text: "Climb alone"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.54}
        on_press:
            root.endGameButtonFunctionality(ClimbAlone)

    MDRectangleFlatButton:
        id: ClimbInHarmony
        md_bg_color: 1, 0, 0, 1
        text: "Climb in harmony"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.41}
        on_press:
            root.endGameButtonFunctionality(ClimbInHarmony)

    MDRectangleFlatButton:
        id: TrapAlone
        md_bg_color: 1, 0, 0, 1
        text: "Trap alone"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.28}
        on_press:
            root.endGameButtonFunctionality(TrapAlone)

    MDRectangleFlatButton:
        id: TrapInHarmony
        md_bg_color: 1, 0, 0, 1
        text: "Trap in harmony"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        on_press:
            root.endGameButtonFunctionality(TrapInHarmony)

    # Next button
    MDRectangleFlatButton:
        pos_hint: {'center_x': 0.85, 'center_y': 0.05}
        text: "Next"
        md_bg_color: 0, 0, 1, 1
        text_color: 1, 1, 1, 1
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'general'

        # Back button
    MDRectangleFlatButton:
        pos_hint: {'center_x': 0.15, 'center_y': 0.05}
        text: "Back"
        md_bg_color: 1, 0, 0, 1
        text_color: 1, 1, 1, 1
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = 'teleop_mid'
"""

Builder.load_string(KV)

class TeleopEndGamePeriod(Screen, DynamicVariables, Constants):
    

    def on_enter(self):
            self.app = App.get_running_app()
            self.screen = self.app.root.get_screen('end')


    def endGameButtonFunctionality(self, selected):
        opinions = [
            self.screen.ids.DidntTry, self.screen.ids.TriedAndFail,
            self.screen.ids.ClimbAlone, self.screen.ids.ClimbInHarmony,
            self.screen.ids.TrapAlone, self.screen.ids.TrapInHarmony
        ]
        select_attr = [
            "isDidntTry", "isTriedAndFail", "isClimbAlone",
            "isClimbInHarmony", "isTrapAlone", "isTrapInHarmony"
        ]
        for i, j in zip(opinions, select_attr):
            if i == selected:
                setattr(DynamicVariables, j, True)
                i.md_bg_color = (1, 0, 1, 1)  # Set color to indicate selection
            else:
                setattr(DynamicVariables, j, False)
                i.md_bg_color = (1, 0, 0, 1)  # Set color to indicate non-selection