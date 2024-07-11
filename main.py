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
                if int(DynamicVariables.auto_amp_count) > 0:
                    DynamicVariables.auto_amp_count = str(int(DynamicVariables.auto_amp_count) - 1)
                label.text = DynamicVariables.auto_amp_count

            case "auto_missed":
                if int(DynamicVariables.auto_missed) > 0:
                    DynamicVariables.auto_missed = str(int(DynamicVariables.auto_missed) - 1)
                label.text = DynamicVariables.auto_missed

            case "teleop_delivery_subtract":
                if int(DynamicVariables.teleop_delivery_count) > 0:
                    DynamicVariables.teleop_delivery_count = str(
                        int(DynamicVariables.teleop_delivery_count) - 1
                    )
                    label.text = DynamicVariables.teleop_delivery_count


    def addition(self, label, addTo):
        match addTo:
            case "auto_amp_count":
                if int(DynamicVariables.auto_amp_count) <= 7:
                    DynamicVariables.auto_amp_count = str(int(DynamicVariables.auto_amp_count) + 1)
                label.text = DynamicVariables.auto_amp_count

            case "auto_missed":
                if int(DynamicVariables.auto_missed) <= 7:
                    DynamicVariables.auto_missed = str(int(DynamicVariables.auto_missed) + 1)
                label.text = DynamicVariables.auto_missed

            case "teleop_speaker_missed":
                DynamicVariables.teleop_speaker_missed_count = str(
                    int(DynamicVariables.teleop_speaker_missed_count) + 1
                )
                DynamicVariables.teleop_current_display_stats = (
                    "scored: "
                    + DynamicVariables.teleop_speaker_scored_count
                    + "\n"
                    + "missed: "
                    + DynamicVariables.teleop_speaker_missed_count
                )
                label.text = DynamicVariables.teleop_current_display_stats

            case "teleop_speaker_scored":
                DynamicVariables.teleop_speaker_scored_count = str(
                    int(DynamicVariables.teleop_speaker_scored_count) + 1
                )
                DynamicVariables.teleop_current_display_stats = (
                    "scored: "
                    + DynamicVariables.teleop_speaker_scored_count
                    + "\n"
                    + "missed: "
                    + DynamicVariables.teleop_speaker_missed_count
                )
                label.text = DynamicVariables.teleop_current_display_stats

            case "teleop_amp_scored":
                DynamicVariables.teleop_amp_scored_count = str(
                    int(DynamicVariables.teleop_amp_scored_count) + 1
                )
                DynamicVariables.teleop_current_display_stats = (
                    "scored: "
                    + DynamicVariables.teleop_amp_scored_count
                    + "\n"
                    + "missed: "
                    + DynamicVariables.teleop_amp_missed_count
                )
                label.text = DynamicVariables.teleop_current_display_stats

            case "teleop_amp_missed":
                DynamicVariables.teleop_amp_missed_count = str(
                    int(DynamicVariables.teleop_amp_missed_count) + 1
                )
                DynamicVariables.teleop_current_display_stats = (
                    "scored: "
                    + DynamicVariables.teleop_amp_scored_count
                    + "\n"
                    + "missed: "
                    + DynamicVariables.teleop_amp_missed_count
                )
                label.text = DynamicVariables.teleop_current_display_stats

            case "teleop_delivery_add":
                DynamicVariables.teleop_delivery_count = str(int(DynamicVariables.teleop_delivery_count) + 1)
                label.text = DynamicVariables.teleop_delivery_count


    def registerFontAndIcons(self):
        LabelBase.register(name="Arial", fn_regular="Sources/hebrew_arial_font.ttf")
        LabelBase.register(name="plus", fn_regular="Sources/plus_icon.svg")
        LabelBase.register(name="minus", fn_regular="Sources/minus_icon.svg")


if __name__ == "__main__":
    ScoutingApp().registerFontAndIcons()
    ScoutingApp().run()
