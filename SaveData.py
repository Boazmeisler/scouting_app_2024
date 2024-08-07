import pyrebase
from Variables import DynamicVariables

class SaveDataClass():
    fireBase = None
    db = None
    firebaseConfig = None
    
    def __init__(self):
        self.firebaseConfig = {
      "apiKey": "AIzaSyADZRWuReRSXjVdpiQHslj04PZp9Xk_UwM",
      "authDomain": "scouting-app-2024-559e2.firebaseapp.com",
      "databaseURL": "https://scouting-app-2024-559e2-default-rtdb.europe-west1.firebasedatabase.app",
      "projectId": "scouting-app-2024-559e2",
      "storageBucket": "scouting-app-2024-559e2.appspot.com",
      "messagingSenderId": "565883178884",
      "appId": "1:565883178884:web:8ecf0977393514416017d1",
      "measurementId": "G-L7PG8P6FGP"
    }
        self.fireBase = pyrebase.initialize_app(self.firebaseConfig)
        self.db = self.fireBase.database()
        
    def saveData(self):
      team = DynamicVariables.groupNumber
      qualificationNumber = DynamicVariables.qualificationNumber + " match"

      data = {
        "scouter Name": DynamicVariables.scouterName,


        "auto amp count": int(DynamicVariables.auto_amp_count),
        "auto missed": int(DynamicVariables.auto_missed),
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
        "robot Passed the Line": DynamicVariables.robot_Passed_the_Line,


        "teleop speaker scored count": int(DynamicVariables.teleop_speaker_scored_count),
        "teleop amp scored count": int(DynamicVariables.teleop_amp_scored_count),
        "teleop speaker missed count": int(DynamicVariables.teleop_speaker_missed_count),
        "teleop amp missed count": int(DynamicVariables.teleop_amp_missed_count),
        "teleop delivery count": int(DynamicVariables.teleop_delivery_count),


        "is didnt try to climb": DynamicVariables.isDidntTry,
        "is tried and fail": DynamicVariables.isTriedAndFail,
        "is climb alone": DynamicVariables.isClimbAlone,
        "is climb in harmony": DynamicVariables.isClimbInHarmony,
        "is trap alone": DynamicVariables.isTrapAlone,
        "is trap in harmony": DynamicVariables.isTrapInHarmony,


        "is defend": DynamicVariables.isDefend,
        "is get defended": DynamicVariables.isGetDefended,
        "is nether": DynamicVariables.isNether,
        
        
        "general information": DynamicVariables.generalInformation
        }

      self.db.child(team).child(qualificationNumber).set(data)
    