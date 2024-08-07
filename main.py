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
from End import KV, EndScreen

Window.size = (300, 630)


class ScoutingApp(MDApp,Constants,DynamicVariables): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.registerFontAndIcons()

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
        screenManager.add_widget(TeleopEndGamePeriod(name="teleop_end"))
        screenManager.add_widget(GeneralInformation(name="general"))
        screenManager.add_widget(EndScreen(name="end"))
  
  
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

    def println(self):
        print('generalInformation: ' + str(DynamicVariables.generalInformation))
        print("scouterName: " + str(DynamicVariables.scouterName))
        print("groupNumber: " + str(DynamicVariables.groupNumber))
        print("qualificationNumber: " + str(DynamicVariables.qualificationNumber))
        print("isDefend: " + str(DynamicVariables.isDefend))
        print("isGetDefended: " + str(DynamicVariables.isGetDefended))
        print("isNether: " + str(DynamicVariables.isNether))
        print("isDidntTry: " + str(DynamicVariables.isDidntTry))
        print("isTriedAndFail: " + str(DynamicVariables.isTriedAndFail))
        print("isClimbAlone: " + str(DynamicVariables.isClimbAlone))
        print("isClimbInHarmony: " + str(DynamicVariables.isClimbInHarmony))
        print("isTrapAlone: " + str(DynamicVariables.isTrapAlone))
        print("isTrapInHarmony: " + str(DynamicVariables.isTrapInHarmony))
        print("stage_note_selected: " + str(DynamicVariables.stage_note_selected))
        print("speaker_note_selected: " + str(DynamicVariables.speaker_note_selected))
        print("amp_note_selected: " + str(DynamicVariables.amp_note_selected))
        print("mid_field_lowest_note_selected: " + str(DynamicVariables.mid_field_lowest_note_selected))
        print("mid_field_low_note_selected: " + str(DynamicVariables.mid_field_low_note_selected))
        print("mid_field_mid_note_selected: " + str(DynamicVariables.mid_field_mid_note_selected))
        print("mid_field_high_note_selected: " + str(DynamicVariables.mid_field_high_note_selected))
        print("mid_field_highest_note_selected: " + str(DynamicVariables.mid_field_highest_note_selected))
        print("A_area_selected: " + str(DynamicVariables.A_area_selected))
        print("B_area_selected: " + str(DynamicVariables.B_area_selected))
        print("C_area_selected: " + str(DynamicVariables.C_area_selected))
        print("D_area_selected: " + str(DynamicVariables.D_area_selected))
        print("auto_amp_count: " + str(DynamicVariables.auto_amp_count))
        print("auto_missed: " + str(DynamicVariables.auto_missed))
        print("robot_Passed_the_Line: " + str(DynamicVariables.robot_Passed_the_Line))
        print("teleop_speaker_scored_count: " + str(DynamicVariables.teleop_speaker_scored_count))
        print("teleop_amp_scored_count: " + str(DynamicVariables.teleop_amp_scored_count))
        print("teleop_delivery_count: " + str(DynamicVariables.teleop_delivery_count))
        print("teleop_speaker_missed_count: " + str(DynamicVariables.teleop_speaker_missed_count))
        print("teleop_amp_missed_count: " + str(DynamicVariables.teleop_amp_missed_count))

if __name__ == "__main__":
    ScoutingApp().run()
