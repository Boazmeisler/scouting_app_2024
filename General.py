from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from Variables import DynamicVariables, Constants


KV = """
<GeneralInformation>:
    name: "general"
    Image:
        source: "Sources/best_defender.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.78}
        size_hint: 0.89, 0.38
        allow_stretch: True
        keep_ratio: False
    MDLabel:
        text: "did the robot ______"
        halign: 'center'
        font_size: "25sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        color: 1, 1, 1, 1
    MDRectangleFlatButton:
        id: defend
        text: "defend"
        md_bg_color: 1,0,0,1
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.85,'center_y': 0.4}
        on_press: root.defendSectionButtonFunctionality(defend)

    MDRectangleFlatButton:
        id: getDefended
        text: "get defended"
        md_bg_color: 1,0,0,1
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5,'center_y': 0.4}
        on_press: root.defendSectionButtonFunctionality(getDefended)

    MDRectangleFlatButton:
        id: neither
        text: "neither"
        md_bg_color: 1,0,0,1
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.15,'center_y': 0.4}
        on_press: root.defendSectionButtonFunctionality(neither)

    MDLabel:
        text: "something to add?"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5,'center_y': 0.28}
        halign: "center"
    MDTextField:
        id: addInformation
        font_name: "Arial"
        halign: "center"
        hint_text: "write here"
        pos_hint:{'center_x': 0.5, 'center_y': 0.23}
        size_hint_x:0.9


    # Next button
    MDRectangleFlatButton:
        pos_hint: {'center_x': 0.85, 'center_y': 0.05}
        text: "finish"
        md_bg_color: 0, 0, 1, 1
        text_color: 1, 1, 1, 1
        on_press:
            root.manager.transition.direction = 'left'
            root.rememberText(addInformation)
            app.println()

        # Back button
    MDRectangleFlatButton:
        pos_hint: {'center_x': 0.15, 'center_y': 0.05}
        text: "Back"
        md_bg_color: 1, 0, 0, 1
        text_color: 1, 1, 1, 1
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = 'end'
"""


Builder.load_string(KV)

class GeneralInformation(Screen, DynamicVariables, Constants):
    def on_enter(self):
        self.app = App.get_running_app()
        self.screen = self.app.root.get_screen('general')


    def defendSectionButtonFunctionality(self, selected):
        opinions = [
            self.screen.ids.defend, self.screen.ids.getDefended, self.screen.ids.neither]
        select_attr = [
            "isDefend", "isGetDefended", "isNether"]
        
        for i, j in zip(opinions, select_attr):
            if i == selected:
                setattr(self.screen, j, True)
                i.md_bg_color = (0, 1, 0, 1)  # Set color to indicate selection
            else:
                setattr(self.screen, j, False)
                i.md_bg_color = (1, 0, 0, 1)  # Set color to indicate non-selection
    

    def rememberText(self, textFild):
        self.inputText = textFild.text[::-1]
    