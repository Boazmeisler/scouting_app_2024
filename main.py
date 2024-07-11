# main.py
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from Variables import DynamicVariables, Constants
from kivy.core.text import LabelBase
from Autonomous import KV, AutonomousPeriod
from Home import KV, HomeScreen
from TeleopMid import KV, TeleopMidGamePeriod
from TeleopEnd import KV, TeleopEndGamePeriod
from General import KV, GeneralInformation
from PreScout import KV, PreScouting

Window.size = (300, 630)


class ScoutingApp(MDApp, DynamicVariables, Constants):


    def build(self):
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        self.add_widgets(sm)
        return sm
    
   
    def add_widgets(self, screenManager):
        screenManager.add_widget(HomeScreen(name="home"))
        screenManager.add_widget(PreScouting(name="preScout"))
        screenManager.add_widget(AutonomousPeriod(name="autonomous_period"))
        screenManager.add_widget(TeleopMidGamePeriod(name="teleop_mid"))
        screenManager.add_widget(TeleopEndGamePeriod(name="end"))
        screenManager.add_widget(GeneralInformation(name="general"))
  
  
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
                    self.teleop_delivery_count = str(
                        int(self.teleop_delivery_count) - 1
                    )
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
                self.teleop_speaker_missed_count = str(
                    int(self.teleop_speaker_missed_count) + 1
                )
                self.teleop_current_display_stats = (
                    "scored: "
                    + self.teleop_speaker_scored_count
                    + "\n"
                    + "missed: "
                    + self.teleop_speaker_missed_count
                )
                label.text = self.teleop_current_display_stats

            case "teleop_speaker_scored":
                self.teleop_speaker_scored_count = str(
                    int(self.teleop_speaker_scored_count) + 1
                )
                self.teleop_current_display_stats = (
                    "scored: "
                    + self.teleop_speaker_scored_count
                    + "\n"
                    + "missed: "
                    + self.teleop_speaker_missed_count
                )
                label.text = self.teleop_current_display_stats

            case "teleop_amp_scored":
                self.teleop_amp_scored_count = str(
                    int(self.teleop_amp_scored_count) + 1
                )
                self.teleop_current_display_stats = (
                    "scored: "
                    + self.teleop_amp_scored_count
                    + "\n"
                    + "missed: "
                    + self.teleop_amp_missed_count
                )
                label.text = self.teleop_current_display_stats

            case "teleop_amp_missed":
                self.teleop_amp_missed_count = str(
                    int(self.teleop_amp_missed_count) + 1
                )
                self.teleop_current_display_stats = (
                    "scored: "
                    + self.teleop_amp_scored_count
                    + "\n"
                    + "missed: "
                    + self.teleop_amp_missed_count
                )
                label.text = self.teleop_current_display_stats

            case "teleop_delivery_add":
                self.teleop_delivery_count = str(int(self.teleop_delivery_count) + 1)
                label.text = self.teleop_delivery_count


    def registerFontAndIcons(self):
        LabelBase.register(name="Arial", fn_regular="Sources/hebrew_arial_font.ttf")
        LabelBase.register(name="plus", fn_regular="Sources/plus_icon.svg")
        LabelBase.register(name="minus", fn_regular="Sources/minus_icon.svg")


    def println(self):
        print(self.inputText)
        print(self.scouterName)
        print(self.groupNumber)
        print(self.qualificationNumber)
        print(self.isDefend )
        print(self.isGetDefended )
        print(self.isNether )
        print(self.isDidntTry )
        print(self.isTriedAndFail )
        print(self.isClimbAlone )
        print(self.isClimbInHarmony )
        print(self.isTrapAlone )
        print(self.isTrapInHarmony )
        print(self.stage_note_selected )
        print(self.speaker_note_selected )
        print(self.amp_note_selected )
        print(self.mid_field_lowest_note_selected )
        print(self.mid_field_low_note_selected )
        print(self.mid_field_mid_note_selected )
        print(self.mid_field_high_note_selected )
        print(self.mid_field_highest_note_selected )
        print(self.A_area_selected )
        print(self.B_area_selected )
        print(self.C_area_selected )
        print(self.D_area_selected )


    auto_amp_count = "0"
    auto_missed = "0"
    robot_Passed_the_Line = None
    teleop_speaker_scored_count = "0"
    teleop_amp_scored_count = "0"
    teleop_speaker_missed_count = "0"
    teleop_amp_missed_count = "0"
    teleop_delivery_count = "0"


if __name__ == "__main__":
    ScoutingApp().registerFontAndIcons()
    ScoutingApp().run()
