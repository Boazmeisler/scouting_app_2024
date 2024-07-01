# main.py
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.core.text import LabelBase

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

#-----------------------------------*******Auto Game********----------------------------------------
<AutonomousPeriod>:
    name: 'autonomous_period'
    FloatLayout: 
        Image:
            source: "Sources/Blue_side.png"
            pos_hint: {'center_x': 0.5, 'center_y': 0.78}
            size_hint: 0.89, 0.38
            allow_stretch: True
            keep_ratio: False

        MDRectangleFlatButton: # stage note
            id: stage_button
            text: ''
            md_bg_color: 1, 0, 1, app.stage_note_transparency
            size_hint_min: None, None
            size_hint: 0.045, 0.02
            pos_hint: {'center_x': app.close_note_line_x, 'center_y': app.stage_note_y}
            on_press: app.buttonFunctionality(stage_button, 'stage_note_transparency')

        MDRectangleFlatButton: # speaker note
            id: speaker_button
            text: ''
            md_bg_color: 1, 0, 1, app.speaker_note_transparency
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.close_note_line_x, 'center_y': app.speaker_note_y}
            on_press: app.buttonFunctionality(speaker_button, 'speaker_note_transparency')

        MDRectangleFlatButton: # amp note
            id: amp_button
            text: ''
            md_bg_color: 1, 0, 1, app.amp_note_transparency
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.close_note_line_x, 'center_y': app.amp_note_y}
            on_press: app.buttonFunctionality(amp_button, 'amp_note_transparency')

        MDRectangleFlatButton: # lowest note mid field
            id: lowest_note_button
            text: ''
            md_bg_color: 1, 0, 1, app.mid_field_lowest_note_transparency
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_field_lowest_note_y}
            on_press: app.buttonFunctionality(lowest_note_button, 'mid_field_lowest_note_transparency')

        MDRectangleFlatButton: # low note mid field
            id: low_note_button
            text: ''
            md_bg_color: 1, 0, 1, app.mid_field_low_note_transparency
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_field_low_note_y}
            on_press: app.buttonFunctionality(low_note_button, 'mid_field_low_note_transparency')

        MDRectangleFlatButton: # mid note mid field
            id: mid_note_button
            text: ''
            md_bg_color: 1, 0, 1, app.mid_field_mid_note_transparency
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_field_mid_note_y}
            on_press: app.buttonFunctionality(mid_note_button, 'mid_field_mid_note_transparency')

        MDRectangleFlatButton: # high mid field
            id: high_note_button
            text: ''
            md_bg_color: 1, 0, 1, app.mid_field_high_note_transparency
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_field_high_note_y}
            on_press: app.buttonFunctionality(high_note_button, 'mid_field_high_note_transparency')

        MDRectangleFlatButton: # highest mid field
            id: highest_note_button
            text: ''
            md_bg_color: 1, 0, 1, app.mid_field_highest_note_transparency
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_field_highest_note_y}
            on_press: app.buttonFunctionality(highest_note_button, 'mid_field_highest_note_transparency')
        MDRectangleFlatButton: # ********A********
            id: A_area
            text: 'A'
            text_color: 0,0,0,1
            font_size: '15sp'
            md_bg_color: 0, 1, 0, app.A_area_transparency
            size_hint_min: None, None
            size_hint: 0.19, 0.14
            pos_hint: {'center_x': app.area_x, 'center_y': app.A_area_y}
            on_press: app.buttonFunctionality(A_area, 'A_area_transparency')
        MDRectangleFlatButton: # ********B********
            id: B_area
            text: 'B'
            text_color: 0,0,0,1
            md_bg_color: 0, 1, 0, app.B_area_transparency
            size_hint_min: None, None
            size_hint: 0.19, 0.01
            pos_hint: {'center_x': app.area_x, 'center_y': app.B_area_y}
            on_press: app.buttonFunctionality(B_area, 'B_area_transparency')
        MDRectangleFlatButton: # ********C********
            id: C_area
            text: 'C'
            text_color: 0,0,0,1
            md_bg_color: 0, 1, 0, app.C_area_transparency
            size_hint_min: None, None
            size_hint: 0.19, 0.05
            pos_hint: {'center_x': app.area_x, 'center_y': app.C_area_y}
            on_press: app.buttonFunctionality(C_area, 'C_area_transparency')
            
        MDRectangleFlatButton: # ********D********
            id: D_area
            text: 'D'
            text_color: 0,0,0,1
            md_bg_color: 0, 1, 0, app.D_area_transparency
            size_hint_min: None, None
            size_hint: 0.19, 0.07
            pos_hint: {'center_x': app.area_x, 'center_y': app.D_area_y}
            on_press: app.buttonFunctionality(D_area, 'D_area_transparency')

        MDLabel:
            text: "Click on the notes that the robot managed to pick up"
            color: 1, 1, 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.55}
            padding: 20
            font_size: "14sp"
            halign: "center"

        # Robot managed in to the amp section
        MDLabel:
            text: "How much did the robot manage into the amp:"
            color: 1, 1, 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.46}
            padding: 20
            font_size: "14sp"
            halign: "center"

        MDFloatingActionButton: # add button
            icon: "plus"
            pos_hint: {'center_x': 0.85, 'center_y': 0.37}
            md_bg_color: 0, 1, 0, 1
            on_press: app.additionNote(note_in_amp, 'amp_count')

        MDFloatingActionButton: # subtract button
            icon: "minus"
            md_bg_color: 1, 0, 0, 1
            pos_hint: {'center_x': 0.15, 'center_y': 0.37}
            on_press: app.SubtractNote(note_in_amp, "amp_count")

        MDBoxLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            size_hint: 0.48, 0.08
            md_bg_color: 1, 1, 1, 1
            radius: 20
            MDLabel:
                id: note_in_amp
                text: str(app.amp_count)
                halign: 'center'
                font_size: "40sp"
                pos_hint: {'center_x': 0.7, 'center_y': 0.5}
                color: 0, 0, 0, 1

        # Robot missed section
        MDLabel:
            text: "How much did the robot miss:"
            color: 1, 1, 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.29}
            padding: 20
            font_size: "14sp"
            halign: "center"

        MDFloatingActionButton: # add button
            icon: "plus"
            pos_hint: {'center_x': 0.85, 'center_y': 0.22}
            md_bg_color: 0, 1, 0, 1
            on_press: app.additionNote(missed_note, "miss_count")

        MDFloatingActionButton: # subtract button
            icon: "minus"
            md_bg_color: 1, 0, 0, 1
            pos_hint: {'center_x': 0.15, 'center_y': 0.22}
            on_press: app.SubtractNote(missed_note, 'miss_count')

        MDBoxLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.22}
            size_hint: 0.48, 0.08
            md_bg_color: 1, 1, 1, 1
            radius: 20
            MDLabel:
                id: missed_note
                text: str(app.miss_count)
                halign: 'center'
                font_size: "40sp"
                pos_hint: {'center_x': 0.7, 'center_y': 0.5}
                color: 0, 0, 0, 1

        # Robot passed the line section
        MDLabel:
            text: "Did the robot pass the line?"
            color: 1, 1, 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.15}
            padding: 20
            font_size: "14sp"
            halign: "center"

        MDRaisedButton:
            text: "Yes"
            pos_hint: {'center_x': 0.32, 'center_y': 0.1}
            md_bg_color: 0, 1, 0, 1
            on_press: app.robotPassedLine(True)

        MDRaisedButton:
            text: "No"
            pos_hint: {'center_x': 0.62, 'center_y': 0.1}
            md_bg_color: 1, 0, 0, 1
            on_press: app.robotPassedLine(False)

        # Next button
        MDRectangleFlatButton:
            pos_hint: {'center_x': 0.85, 'center_y': 0.05}
            text: "Next"
            md_bg_color: 0, 0, 1, 1
            text_color: 1, 1, 1, 1
            on_press: root.manager.current = 'teleop_mid'

#----------------------------------********Mid Game********-------------------------------------------
<TeleopMidGamePeriod>:
    name: 'teleop_mid'
    MDBoxLayout:
#-----------------------------------*******End Game********--------------------------------------------
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

        self.close_note_line_x = 0.336
        self.far_note_line_x = 0.858
        self.area_x = 0.15

        self.stage_note_y = 0.78
        self.speaker_note_y = 0.848
        self.amp_note_y = 0.915
        self.mid_field_lowest_note_y = 0.624
        self.mid_field_low_note_y = 0.702
        self.mid_field_mid_note_y = 0.78
        self.mid_field_high_note_y = 0.858
        self.mid_field_highest_note_y = 0.935
        self.A_area_y = 0.695
        self.B_area_y = 0.795
        self.C_area_y = 0.848
        self.D_area_y = 0.91

        # Set transparency levels
        self.stage_note_transparency = 0.1
        self.speaker_note_transparency = 0.1
        self.amp_note_transparency = 0.1
        self.mid_field_lowest_note_transparency = 0.1
        self.mid_field_low_note_transparency = 0.1
        self.mid_field_mid_note_transparency = 0.1
        self.mid_field_high_note_transparency = 0.1
        self.mid_field_highest_note_transparency = 0.1
        self.A_area_transparency = 0.1
        self.B_area_transparency = 0.1
        self.C_area_transparency = 0.1
        self.D_area_transparency = 0.1

        self.amp_count = "0"
        self.miss_count = "0"
        self.robot_Passed_the_Line = False

        self.theme_cls.theme_style = "Dark"

        screen = Builder.load_string(KV)
        return screen

    def robotPassedLine(self, isPassedLine):
        self.robot_Passed_the_Line = isPassedLine

    def buttonFunctionality(self, button, transparency_attr):
        current_transparency = getattr(self, transparency_attr, 0.1)
        if current_transparency == 1:
            setattr(self, transparency_attr, 0.1)
        else:
            setattr(self, transparency_attr, 1)
        button.md_bg_color = (1, 0, 1, getattr(self, transparency_attr))

    def SubtractNote(self, label, SubtractFrom):
        if SubtractFrom == "amp_count":
            if int(self.amp_count) > 0:
                self.amp_count = str(int(self.amp_count) - 1)
            label.text = self.amp_count
        else:
            if int(self.miss_count) > 0:
                self.miss_count = str(int(self.miss_count) - 1)
            label.text = self.miss_count

    def additionNote(self, label, addTo):
        if addTo == "amp_count":
            if int(self.amp_count) <= 7:
                self.amp_count = str(int(self.amp_count) + 1)
            label.text = self.amp_count
        else:
            if int(self.miss_count) <= 4:
                self.miss_count = str(int(self.miss_count) + 1)
            label.text = self.miss_count


if __name__ == "__main__":
    ScoutingApp().run()
