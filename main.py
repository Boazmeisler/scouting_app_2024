# main.py
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.core.text import LabelBase
from Variables import Constants,DynamicVariables
from Autonomous import KV as autonomous_KV
from Home import KV as home_KV
from TeleopMid import KV as teleopMid_KV
from TeleopEnd import KV as teleopEnd_KV

Window.size = (300, 630)
LabelBase.register(name="plus", fn_regular="Sources/plus_icon.svg")
LabelBase.register(name="minus", fn_regular="Sources/minus_icon.svg")
KV = """
ScreenManager:
    HomeScreen:
    AutonomousPeriod:
    TeleopMidGamePeriod:
    TeleopEndGamePeriod:
"""


class HomeScreen(Screen):
    pass


class AutonomousPeriod(Screen):
    pass


class TeleopEndGamePeriod(Screen):
    pass


class TeleopMidGamePeriod(Screen):
    pass


class ScoutingApp(MDApp,Constants,DynamicVariables):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Builder.load_string(KV)
        Builder.load_string(autonomous_KV)
        Builder.load_string(home_KV)
        Builder.load_string(teleopMid_KV)
        Builder.load_string(teleopEnd_KV)
        
        
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name = "home"))
        sm.add_widget(AutonomousPeriod(name = "autonomous_period"))
        sm.add_widget(TeleopMidGamePeriod(name = "teleop_mid"))
        sm.add_widget(TeleopEndGamePeriod(name = "end"))
        
        return sm

    def robotPassedLine(self, isPassedLine):
        self.robot_Passed_the_Line = isPassedLine

    def autoStartAreaButtonFunctionality(self, disableArea, enableArea, transparency_attr):
        setattr(self, transparency_attr[0], 1)
        enableArea.md_bg_color = (1,0,1,getattr(self,transparency_attr[0]))
        for i, j in zip(disableArea, transparency_attr[1:]):
            setattr(self, j, 0.1)
            i.md_bg_color = (1, 0, 1, getattr(self, j))


    def autoSelectFunctionality(self, button, transparency_attr):
        current_transparency = getattr(self, transparency_attr, 0.1)
        if current_transparency == 1:
            setattr(self, transparency_attr, 0.1)
        else:
            setattr(self, transparency_attr, 1)
        button.md_bg_color = (1, 0, 1, getattr(self, transparency_attr))





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
              

    def endGameButtonFunctionality(self, selected, opinions):
        select_attr = ["isDidntTry","isTriedAndFail","isClimbAlone","isClimbInHarmony","isTrapAlone","isTrapInHarmony",]
        for i,j in zip(opinions,select_attr):
            if i == selected:
                setattr(self, j, 1)
                i.md_bg_color = (1, 0, getattr(self,j), 1)
            else:
                setattr(self, j, 0)
                i.md_bg_color = (1, 0, getattr(self,j), 1)
              
if __name__ == "__main__":
    ScoutingApp().run()