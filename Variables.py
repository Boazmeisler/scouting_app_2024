class Constants():
    close_note_line_x = 0.664
    far_note_line_x = 0.142
    area_x = 0.85

    stage_note_y = 0.779
    speaker_note_y = 0.712
    amp_note_y = 0.644
    mid_field_lowest_note_y = 0.624
    mid_field_low_note_y = 0.702
    mid_field_mid_note_y = 0.78
    mid_field_high_note_y = 0.858
    mid_field_highest_note_y = 0.935
    A_area_y = 0.87
    B_area_y = 0.77
    C_area_y = 0.71
    D_area_y = 0.645

    teams =[
    "1574-MisCar",
    "1576-Voltrix",
    "1577-Steampunk",
    "1580-The Blue Monkeys",
    "1657-Hamosad",
    "1690-Orbit",
    "1937-Elysium",
    "1942-Cinderella Tel-Nof",
    "1943-Neat Team",
    "1954-ElectroBunny",
    "2096-RoboActive",
    "2212-The Spikes",
    "2230-General Angels",
    "2231-OnyxTronix",
    "2630-Thunderbolts",
    "2679-Atlantis",
    "3034-Galileo",
    "3065-Jatt High School",
    "3075-Ha-Dream Team",
    "3083-Artemis",
    "3211-The Y Team",
    "3316-D-Bug",
    "3339-BumbleB",
    "3388-Flash in memory of Margarita Gusak",
    "3835-Vulcan",
    "4319-Ladies FIRST",
    "4320-The Joker",
    "4338-Falcons",
    "4416-Skynet",
    "4586-PRIMO",
    "4590-GreenBlitz",
    "4661-The Red Pirates",
    "4744-Ninjas",
    "5135-Black Unicorns",
    "5291-Emperius",
    "5554-Poros",
    "5614-Team Sycamore",
    "5635-Demacia",
    "5654-Phoenix",
    "5715-DRC",
    "5747-Athena",
    "5928-MetalBoost",
    "5951-Makers Assemble",
    "5987-Galaxia",
    "5990-TRIGON",
    "6049-Pegasus",
    "6104-Desert Eagles",
    "6168-alzahrawi",
    "6230-Team Koi",
    "6738-Excalibur",
    "6740-G3",
    "6741-Space monkeys",
    "7039-XO",
    "7067-Team Streak",
    "7112-EverGreen",
    "7177-Amal tayibe",
    "7554-Green Rockets",
    "7845-8BIT",
    "8175-Piece of Mind",
    "8223-Mariners",
    "8843-Amal",
    "9303-PORTAL",
    "9304-legend's",
    "9738-Ionic Bond",
    "9739-Firefly",
    "9740-CAN://Bus",
    "9741-STORM"
]



class DynamicVariables():

    generalInformation = None 

    scouterName = None
    groupNumber = None
    qualificationNumber = None

    isDefend = False
    isGetDefended = False
    isNether = False

    isDidntTry = False
    isTriedAndFail = False
    isClimbAlone = False
    isClimbInHarmony = False
    isTrapAlone = False
    isTrapInHarmony = False

    stage_note_selected = False
    speaker_note_selected = False
    amp_note_selected = False
    mid_field_lowest_note_selected = False
    mid_field_low_note_selected = False
    mid_field_mid_note_selected = False
    mid_field_high_note_selected = False
    mid_field_highest_note_selected = False
    A_area_selected = False
    B_area_selected = False
    C_area_selected = False
    D_area_selected = False


    auto_amp_count = "0"
    auto_missed = "0"
    robot_Passed_the_Line = None
    teleop_speaker_scored_count = "0"
    teleop_amp_scored_count = "0"
    teleop_speaker_missed_count = "0"
    teleop_amp_missed_count = "0"
    teleop_delivery_count = "0"

        
    teleop_current_display_stats = "scored: 0" + "\n" + "missed: 0"