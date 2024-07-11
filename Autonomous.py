from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from Variables import DynamicVariables, Constants

KV = """
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
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.045, 0.02
            pos_hint: {'center_x': app.close_note_line_x, 'center_y': app.stage_note_y}
            on_press: root.autoSelectFunctionality(stage_button, 'stage_note_selected')

        MDRectangleFlatButton: # speaker note
            id: speaker_button
            text: ''
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.close_note_line_x, 'center_y': app.speaker_note_y}
            on_press: root.autoSelectFunctionality(speaker_button, 'speaker_note_selected')

        MDRectangleFlatButton: # amp note
            id: amp_button
            text: ''
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.close_note_line_x, 'center_y': app.amp_note_y}
            on_press: root.autoSelectFunctionality(amp_button, 'amp_note_selected')

        MDRectangleFlatButton: # lowest note mid field
            id: lowest_note_button
            text: ''
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_field_lowest_note_y}
            on_press: root.autoSelectFunctionality(lowest_note_button, 'mid_field_lowest_note_selected')

        MDRectangleFlatButton: # low note mid field
            id: low_note_button
            text: ''
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_field_low_note_y}
            on_press: root.autoSelectFunctionality(low_note_button, 'mid_field_low_note_selected')

        MDRectangleFlatButton: # mid note mid field
            id: mid_note_button
            text: ''
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_field_mid_note_y}
            on_press: root.autoSelectFunctionality(mid_note_button, 'mid_field_mid_note_selected')

        MDRectangleFlatButton: # high mid field
            id: high_note_button
            text: ''
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_field_high_note_y}
            on_press: root.autoSelectFunctionality(high_note_button, 'mid_field_high_note_selected')

        MDRectangleFlatButton: # highest mid field
            id: highest_note_button
            text: ''
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.045,0.02
            pos_hint: {'center_x': app.far_note_line_x, 'center_y': app.mid_field_highest_note_y}
            on_press: root.autoSelectFunctionality(highest_note_button, 'mid_field_highest_note_selected')
        MDRectangleFlatButton: # ********A********
            id: A_area
            text: 'A'
            text_color: 0,0,0,1
            font_size: '15sp'
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.19, 0.14
            pos_hint: {'center_x': app.area_x, 'center_y': app.A_area_y}
            on_press: root.autoStartAreaButtonFunctionality(A_area) 
 
        MDRectangleFlatButton: # ********B********
            id: B_area
            text: 'B'
            text_color: 0,0,0,1
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.19, 0.01
            pos_hint: {'center_x': app.area_x, 'center_y': app.B_area_y}
            on_press: root.autoStartAreaButtonFunctionality(B_area)
 

        MDRectangleFlatButton: # ********C********
            id: C_area
            text: 'C'
            text_color: 0,0,0,1
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.19, 0.05
            pos_hint: {'center_x': app.area_x, 'center_y': app.C_area_y}
            on_press: root.autoStartAreaButtonFunctionality(C_area)
 

            
        MDRectangleFlatButton: # ********D********
            id: D_area
            text: 'D'
            text_color: 0,0,0,1
            md_bg_color: 1, 0, 1, 0.1
            size_hint_min: None, None
            size_hint: 0.19, 0.07
            pos_hint: {'center_x': app.area_x, 'center_y': app.D_area_y}
            on_press: root.autoStartAreaButtonFunctionality(D_area)
 


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
            on_press: app.addition(note_in_amp, 'auto_amp_count')

        MDFloatingActionButton: # subtract button
            icon: "minus"
            md_bg_color: 1, 0, 0, 1
            pos_hint: {'center_x': 0.15, 'center_y': 0.37}
            on_press: app.subtract(note_in_amp, "auto_amp_count")

        MDBoxLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            size_hint: 0.48, 0.08
            md_bg_color: 1, 1, 1, 1
            radius: 20
            MDLabel:
                id: note_in_amp
                text: app.auto_amp_count
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
            on_press: app.addition(missed_note, "auto_missed")

        MDFloatingActionButton: # subtract button
            icon: "minus"
            md_bg_color: 1, 0, 0, 1
            pos_hint: {'center_x': 0.15, 'center_y': 0.22}
            on_press: app.subtract(missed_note, 'auto_missed')

        MDBoxLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.22}
            size_hint: 0.48, 0.08
            md_bg_color: 1, 1, 1, 1
            radius: 20
            MDLabel:
                id: missed_note
                text: str(app.auto_missed)
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
            id: passLine
            text: "Yes"
            pos_hint: {'center_x': 0.32, 'center_y': 0.1}
            md_bg_color: 1, 0, 0, 1
            on_press: root.robotPassedLine(True)

        MDRaisedButton:
            id: didntPassLine
            text: "No"
            pos_hint: {'center_x': 0.62, 'center_y': 0.1}
            md_bg_color: 1, 0, 0, 1
            on_press: root.robotPassedLine(False)

        # Next button
        MDRectangleFlatButton:
            pos_hint: {'center_x': 0.85, 'center_y': 0.05}
            text: "Next"
            md_bg_color: 0, 0, 1, 1
            text_color: 1, 1, 1, 1
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'teleop_mid'

"""


Builder.load_string(KV)

class AutonomousPeriod(Screen, DynamicVariables, Constants):
    
    
    def on_enter(self):
        self.app = App.get_running_app()
        self.screen = self.app.root.get_screen('autonomous_period')


    def robotPassedLine(self, isPassedLine):
        self.robot_Passed_the_Line = isPassedLine
        
        if isPassedLine:
            self.screen.ids.didntPassLine.md_bg_color = (1,0,0,1)
            self.screen.ids.passLine.md_bg_color = (0,1,0,1)
        else:
            self.screen.ids.didntPassLine.md_bg_color = (0,1,0,1)
            self.screen.ids.passLine.md_bg_color = (1,0,0,1)

            
    def autoStartAreaButtonFunctionality(self, enableArea):
        selected_attr = ["A_area_selected   ", "B_area_selected",
                         "C_area_selected   ", "D_area_selected"]
        
        opinions = [self.screen.ids.A_area, self.screen.ids.B_area,
                    self.screen.ids.C_area, self.screen.ids.D_area]
            
        for i, j in zip(opinions,selected_attr):
            if i == enableArea:
                setattr(self, j, 1)
                i.md_bg_color = (1,0,1,1)
            else:
                setattr(self, j, 0.1)
                i.md_bg_color = (1,0,1,0.1)


    def autoSelectFunctionality(self, button, selected_attr):
        current_selected = getattr(self, selected_attr)
        if current_selected:
            setattr(self, selected_attr, False)
            button.md_bg_color = (1, 0, 1, 0.1)
        else:
            setattr(self, selected_attr, True)
            button.md_bg_color = (1, 0, 1, 1)