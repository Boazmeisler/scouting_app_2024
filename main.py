# main.py
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.core.text import LabelBase
from Variables import Constants,DynamicVariables
from Autonomous import KV
from Home import KV
from TeleopMid import KV
from TeleopEnd import KV
from General import KV
from PreScout import KV

Window.size = (300, 630)

LabelBase.register(name='Arial', fn_regular="Sources/hebrew_arial_font.ttf")

LabelBase.register(name="plus", fn_regular="Sources/plus_icon.svg")
LabelBase.register(name="minus", fn_regular="Sources/minus_icon.svg")

class HomeScreen(Screen):
    pass

class PreScouting(Screen):
    pass

class AutonomousPeriod(Screen):
    pass


class TeleopMidGamePeriod(Screen):
    pass


class TeleopEndGamePeriod(Screen):
    pass


class GeneralInformation(Screen):
    pass



class ScoutingApp(MDApp,Constants,DynamicVariables):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name = "home"))
        sm.add_widget(PreScouting(name = "preScout"))
        sm.add_widget(AutonomousPeriod(name = "autonomous_period"))
        sm.add_widget(TeleopMidGamePeriod(name = "teleop_mid"))
        sm.add_widget(TeleopEndGamePeriod(name = "end"))
        sm.add_widget(GeneralInformation(name = "general"))
        
        return sm

    def robotPassedLine(self, isPassedLine, button):
        screen = self.root.get_screen('autonomous_period')
        self.robot_Passed_the_Line = isPassedLine
        if isPassedLine:
            screen.ids.didntPassLine.md_bg_color = (1,0,0,1)
            screen.ids.passLine.md_bg_color = (0,1,0,1)
        else:
            screen.ids.didntPassLine.md_bg_color = (0,1,0,1)
            screen.ids.passLine.md_bg_color = (1,0,0,1)
            
    def autoStartAreaButtonFunctionality(self, enableArea):
        screen = self.root.get_screen('autonomous_period')
        
        selected_attr = ["A_area_selected   ", "B_area_selected",
                         "C_area_selected   ", "D_area_selected"]
        
        opinions = [screen.ids.A_area, screen.ids.B_area,
                    screen.ids.C_area, screen.ids.D_area]
        
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


    def subtract(self, label, subtractFrom):
        match subtractFrom:
            case "auto_amp_count":
                if int(self.auto_amp_count) > 0:
                    self.auto_amp_count = str(int(self.auto_amp_count) - 1)
                label.text = self.auto_amp_count
                
            case "auto_missed":
                if int(self.auto_missed) > 0:
                    self.auto_missed = str(int(self.auto_missed) - 1)
                label.text = self.auto_missed
            
            case "teleop_delivery_subtract":
                if int(self.teleop_delivery_count) > 0:
                    self.teleop_delivery_count = str(int(self.teleop_delivery_count) - 1)
                    label.text = self.teleop_delivery_count

    def addition(self, label, addTo):
        match addTo:
            case "auto_amp_count":
                if int(self.auto_amp_count) <= 7:
                    self.auto_amp_count = str(int(self.auto_amp_count) + 1)
                label.text = self.auto_amp_count
            
            case "auto_missed":
                if int(self.auto_missed) <= 7:
                    self.auto_missed = str(int(self.auto_missed) + 1)
                label.text = self.auto_missed
            
            case "teleop_speaker_missed":
                self.teleop_speaker_missed_count = str(int(self.teleop_speaker_missed_count) + 1)
                self.teleop_current_display_stats = "scored: " + self.teleop_speaker_scored_count + "\n" + "missed: " + self.teleop_speaker_missed_count
                label.text = self.teleop_current_display_stats
                
            case "teleop_speaker_scored":
              self.teleop_speaker_scored_count = str(int(self.teleop_speaker_scored_count) + 1)
              self.teleop_current_display_stats = "scored: " + self.teleop_speaker_scored_count + "\n" + "missed: " + self.teleop_speaker_missed_count
              label.text = self.teleop_current_display_stats
            
            case "teleop_amp_scored":
                self.teleop_amp_scored_count = str(int(self.teleop_amp_scored_count) + 1)
                self.teleop_current_display_stats = "scored: " + self.teleop_amp_scored_count + "\n" + "missed: " + self.teleop_amp_missed_count
                label.text = self.teleop_current_display_stats

            case "teleop_amp_missed":
                self.teleop_amp_missed_count = str(int(self.teleop_amp_missed_count) + 1)
                self.teleop_current_display_stats = "scored: " + self.teleop_amp_scored_count + "\n" + "missed: " + self.teleop_amp_missed_count
                label.text = self.teleop_current_display_stats
            
            case "teleop_delivery_add":
                self.teleop_delivery_count = str(int(self.teleop_delivery_count) + 1)
                label.text = self.teleop_delivery_count
              

    def endGameButtonFunctionality(self, selected):
        screen = self.root.get_screen('end')
        opinions = [
            screen.ids.DidntTry, screen.ids.TriedAndFail,
            screen.ids.ClimbAlone, screen.ids.ClimbInHarmony,
            screen.ids.TrapAlone, screen.ids.TrapInHarmony
        ]
        select_attr = [
            "isDidntTry", "isTriedAndFail", "isClimbAlone",
            "isClimbInHarmony", "isTrapAlone", "isTrapInHarmony"
        ]
        for i, j in zip(opinions, select_attr):
            if i == selected:
                setattr(screen, j, 1)
                i.md_bg_color = (1, 0, 1, 1)  # Set color to indicate selection
            else:
                setattr(screen, j, 0)
                i.md_bg_color = (1, 0, 0, 1)  # Set color to indicate non-selection

    def defendSectionButtonFunctionality(self, selected):
        screen = self.root.get_screen('general')
        opinions = [
            screen.ids.defend, screen.ids.getDefended, screen.ids.neither]
        select_attr = [
            "isDefend", "isGetDefended", "isNether"]
        
        for i, j in zip(opinions, select_attr):
            if i == selected:
                setattr(screen, j, True)
                i.md_bg_color = (0, 1, 0, 1)  # Set color to indicate selection
            else:
                setattr(screen, j, False)
                i.md_bg_color = (1, 0, 0, 1)  # Set color to indicate non-selection
    
    def rememberText(self, textFild):
        self.inputText = textFild.text[::-1]
    
    def rememberPreScout(self):
        screen = self.root.get_screen('preScout')
        self.scouterName = screen.ids.scouter_name.text[::-1]
        self.groupNumber = screen.ids.group_num.text
        self.qualificationNumber = screen.ids.qualification_num.text


            
if __name__ == "__main__":
    ScoutingApp().run()