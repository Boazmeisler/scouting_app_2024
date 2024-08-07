import pyrebase
from Variables import DynamicVariables

firebaseConfig = {
  "apiKey": "AIzaSyADZRWuReRSXjVdpiQHslj04PZp9Xk_UwM",
  "authDomain": "scouting-app-2024-559e2.firebaseapp.com",
  "databaseURL": "https://scouting-app-2024-559e2-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "scouting-app-2024-559e2",
  "storageBucket": "scouting-app-2024-559e2.appspot.com",
  "messagingSenderId": "565883178884",
  "appId": "1:565883178884:web:8ecf0977393514416017d1",
  "measurementId": "G-L7PG8P6FGP"
}
class SaveData():
    fireBase = None
    db = None
    data = None
    def __init__(self):
        self.fireBase = pyrebase.initialize_app(firebaseConfig)
        self.db = self.fireBase.database()
        self.data = {
            "qualificationNumber": DynamicVariables.qualificationNumber,
            "scouterName": DynamicVariables.scouterName,
            "auto amp_count": DynamicVariables.auto_amp_count,
            "auto missed": DynamicVariables.auto_missed,
            "auto speaker count": int(DynamicVariables.auto_count) - int(DynamicVariables.auto_missed) - int(DynamicVariables.auto_amp_count),
            "A area selected: ": DynamicVariables.A_area_selected,
            "B area selected: ": DynamicVariables.B_area_selected,
            "C area selected: ": DynamicVariables.C_area_selected,
            "D area selected: ": DynamicVariables.D_area_selected,
            "stage note selected": DynamicVariables.stage_note_selected,
            "speaker note selected": DynamicVariables.speaker_note_selected,
            "amp note selected": DynamicVariables.amp_note_selected,
            "mid field lowest note selected": DynamicVariables.mid_field_lowest_note_selected,
            "mid field low note selected": DynamicVariables.mid_field_low_note_selected,
            "mid field mid note selected": DynamicVariables.mid_field_mid_note_selected,
            "mid field high note selected": DynamicVariables.mid_field_high_note_selected,
            "mid field highest note selected": DynamicVariables.mid_field_highest_note_selected,
            "robot Passed the Line": DynamicVariables.robot_passed_the_line
        }

    