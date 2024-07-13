import firebase_admin
from Variables import DynamicVariables
from firebase_admin import credentials, firestore


class SaveData:
    def __init__(self):
        self.data = {
            'generalInformation': DynamicVariables.generalInformation,
            'scouterName': DynamicVariables.scouterName,
            'groupNumber': DynamicVariables.groupNumber,
            'qualificationNumber': DynamicVariables.qualificationNumber,
            'isDefend': DynamicVariables.isDefend,
            'isGetDefended': DynamicVariables.isGetDefended,
            'isNether': DynamicVariables.isNether,
            'isDidntTry': DynamicVariables.isDidntTry,
            'isTriedAndFail': DynamicVariables.isTriedAndFail,
            'isClimbAlone': DynamicVariables.isClimbAlone,
            'isClimbInHarmony': DynamicVariables.isClimbInHarmony,
            'isTrapAlone': DynamicVariables.isTrapAlone,
            'isTrapInHarmony': DynamicVariables.isTrapInHarmony,
            'stage_note_selected': DynamicVariables.stage_note_selected,
            'speaker_note_selected': DynamicVariables.speaker_note_selected,
            'amp_note_selected': DynamicVariables.amp_note_selected,
            'mid_field_lowest_note_selected': DynamicVariables.mid_field_lowest_note_selected,
            'mid_field_low_note_selected': DynamicVariables.mid_field_low_note_selected,
            'mid_field_mid_note_selected': DynamicVariables.mid_field_mid_note_selected,
            'mid_field_high_note_selected': DynamicVariables.mid_field_high_note_selected,
            'mid_field_highest_note_selected': DynamicVariables.mid_field_highest_note_selected,
            'A_area_selected': DynamicVariables.A_area_selected,
            'B_area_selected': DynamicVariables.B_area_selected,
            'C_area_selected': DynamicVariables.C_area_selected,
            'D_area_selected': DynamicVariables.D_area_selected,
            'auto_amp_count': DynamicVariables.auto_amp_count,
            'auto_missed': DynamicVariables.auto_missed,
            'robot_Passed_the_Line': DynamicVariables.robot_Passed_the_Line,
            'teleop_speaker_scored_count': DynamicVariables.teleop_speaker_scored_count,
            'teleop_amp_scored_count': DynamicVariables.teleop_amp_scored_count,
            'teleop_speaker_missed_count': DynamicVariables.teleop_speaker_missed_count,
            'teleop_amp_missed_count': DynamicVariables.teleop_amp_missed_count,
            'teleop_delivery_count': DynamicVariables.teleop_delivery_count,
        }

        self.db = self.initialize_firebase()
        self.collection_name = "scouting_data"


    def initialize_firebase(self):
        cred = credentials.Certificate("scouting-app-2024-adminsdk.json")
        firebase_admin.initialize_app(cred)
        return firestore.client()
    

    def add_data(self):
        self.db.collection(self.collection_name).add(self.data)
