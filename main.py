# main.py
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivymd.icon_definitions import md_icons

Window.size = (300, 630)
LabelBase.register(name="plus", fn_regular="Sources/plus_icon.svg")
LabelBase.register(name="minus", fn_regular="Sources/minus_icon.svg")


KV = """
ScreenManager:
    HomeScreen:
    AutonomousPeriod:
    TeleopMidGamePeriod:
    TeleopEndGamePeriod:

<HomeScreen>:
    name: 'home'
    MDRectangleFlatButton:
        text: 'Start new scouting trip'
        text_color: 0, 0, 0, 1
        md_bg_color: 1, 0, 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.07}
        on_press: root.manager.current = 'autonomous_period'
    Image:
        source: "Sources/FRC_fild_Image.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        size_hint: 0.95, 1
    Image:
        source: "Sources/grop_logo.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.77}
        size_hint: 0.95, 1

<AutonomousPeriod>:
    name: 'autonomous_period'
    Image:
        source: "Sources/Blue_side.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.78}
        size_hint: 0.95, 1
    MDRectangleFlatButton: #stage note
        id: stage_button
        text: ''
        md_bg_color: 1, 0, 1, app.stage_note_transparency
        size_hint: None, None
        size: 20, 20
        pos_hint: {'center_x': app.close_note_line_x, 'center_y': app.stage_note_y}
        on_press: app.buttonFunctionality(stage_button, 'stage_note_transparency')
    MDRectangleFlatButton: #speeker note
        id: speker_button
        text: ''
        md_bg_color: 1, 0, 1, app.speker_note_transparency
        size_hint: None, None
        size: 20, 20
        pos_hint: {'center_x': app.close_note_line_x, 'center_y': app.speker_note_y}
        on_press: app.buttonFunctionality(speker_button, 'speker_note_transparency')
    MDRectangleFlatButton: #amp note
        id: amp_button
        text: ''
        md_bg_color: 1, 0, 1, app.amp_note_transparency
        size_hint: None, None
        size: 20, 20
        pos_hint: {'center_x': app.close_note_line_x, 'center_y': app.amp_note_y}
        on_press: app.buttonFunctionality(amp_button, 'amp_note_transparency')
    MDRectangleFlatButton: #lowest note mid field
        id: lowest_note_button
        text: ''
        md_bg_color: 1, 0, 1, app.mid_fild_lowest_note_transparency
        size_hint: None, None
        size: 20, 20
        pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_fild_lowest_note_y}
        on_press: app.buttonFunctionality(lowest_note_button, 'mid_fild_lowest_note_transparency')
    MDRectangleFlatButton: #low note mid field
        id: low_note_button
        text: ''
        md_bg_color: 1, 0, 1, app.mid_fild_low_note_transparency
        size_hint: None, None
        size: 20, 20
        pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_fild_low_note_y}
        on_press: app.buttonFunctionality(low_note_button, 'mid_fild_low_note_transparency')
    MDRectangleFlatButton: #mid note mid field
        id: mid_note_button
        text: ''
        md_bg_color: 1, 0, 1, app.mid_fild_mid_note_transparency
        size_hint: None, None
        size: 20, 20
        pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_fild_mid_note_y}
        on_press: app.buttonFunctionality(mid_note_button, 'mid_fild_mid_note_transparency')
    MDRectangleFlatButton: #high mid field
        id: high_note_button
        text: ''
        md_bg_color: 1, 0, 1, app.mid_fild_high_note_transparency
        size_hint: None, None
        size: 20, 20
        pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_fild_high_note_y}
        on_press: app.buttonFunctionality(high_note_button, 'mid_fild_high_note_transparency')
    MDRectangleFlatButton: #highest mid field
        id: highest_note_button
        text: ''
        md_bg_color: 1, 0, 1, app.mid_fild_highest_note_transparency
        size_hint: None, None
        size: 20, 20
        pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_fild_highest_note_y}
        on_press: app.buttonFunctionality(highest_note_button, 'mid_fild_highest_note_transparency')
    MDLabel:
        text: "Click on the notes that the robot managed to shoot in to the speaker/amp"
        color: 1, 1, 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
        padding: 20
        font_size: "14sp"
        halign: "center"
    MDLabel:
        text: "How much did the robot managed in to the amp:"
        color: 1, 1, 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        padding: 20
        font_size: "18sp"
        halign: "center"
    MDFloatingActionButton: #add button
        icon: "plus"
        pos_hint: {'center_x': 0.85, 'center_y': 0.3}
        md_bg_color: 0, 1, 0, 1
        on_press: app.additionNoteToAmp(note_in_app)
    MDFloatingActionButton: #subtract button
        icon: "minus"
        md_bg_color: 1, 0, 0, 1
        pos_hint: {'center_x': 0.15, 'center_y': 0.3}
        on_press: app.SubtractNoteFromAmp(note_in_app)
    MDBoxLayout:
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        size_hint: 0.48,0.08
        md_bg_color: 1,1,1,1
        radius: 20
        MDLabel:
            id: note_in_app
            text: app.amp_count
            halign: 'center'
            font_size: "40sp"
            pos_hint: {'center_x': 0.7, 'center_y': 0.5}
            color: 0,0,0,1


<TeleopMidGamePeriod>:
    name: 'teleop_mid'

<TeleopEndGamePeriod>:
    name: 'end'
"""


class HomeScreen(Screen):
    pass


class AutonomousPeriod(Screen):
    pass


class TeleopMidGamePeriod(Screen):
    pass


class TeleopEndGamePeriod(Screen):
    pass


class ScoutingApp(MDApp):
    def build(self):
        self.close_note_line_x = 0.325
        self.far_note_line_x = 0.879
        self.stage_note_y = 0.78
        self.speker_note_y = 0.852
        self.amp_note_y = 0.922
        self.mid_fild_lowest_note_y = 0.615
        self.mid_fild_low_note_y = 0.698
        self.mid_fild_mid_note_y = 0.78
        self.mid_fild_high_note_y = 0.862
        self.mid_fild_highest_note_y = 0.945

        # Set transparency levels
        self.stage_note_transparency = 0.1
        self.speker_note_transparency = 0.1
        self.amp_note_transparency = 0.1
        self.mid_fild_lowest_note_transparency = 0.1
        self.mid_fild_low_note_transparency = 0.1
        self.mid_fild_mid_note_transparency = 0.1
        self.mid_fild_high_note_transparency = 0.1
        self.mid_fild_highest_note_transparency = 0.1

        self.amp_count = "0"

        self.theme_cls.theme_style = "Dark"

        screen = Builder.load_string(KV)
        return screen

    def buttonFunctionality(self, button, transparency_attr):
        current_transparency = getattr(self, transparency_attr, 0.1)
        if current_transparency == 1:
            setattr(self, transparency_attr, 0.1)
        else:
            setattr(self, transparency_attr, 1)
        button.md_bg_color = (1, 0, 1, getattr(self, transparency_attr))

    def SubtractNoteFromAmp(self, label):
        if int(self.amp_count) > 0:
            self.amp_count = str(int(self.amp_count) - 1)
        label.text = self.amp_count

    def additionNoteToAmp(self, label):
        if int(self.amp_count) <= 5:
            self.amp_count = str(int(self.amp_count) + 1)
        label.text = self.amp_count


if __name__ == "__main__":
    ScoutingApp().run()
