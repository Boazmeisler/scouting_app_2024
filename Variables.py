class Constants:
    close_note_line_x = 0.664
    far_note_line_x = 0.142
    area_x = 0.85

    stage_note_y = 0.644
    speaker_note_y = 0.712
    amp_note_y = 0.779
    mid_field_lowest_note_y = 0.624
    mid_field_low_note_y = 0.702
    mid_field_mid_note_y = 0.78
    mid_field_high_note_y = 0.858
    mid_field_highest_note_y = 0.935
    A_area_y = 0.87
    B_area_y = 0.77
    C_area_y = 0.71
    D_area_y = 0.645

    teams = [
        "1574-MisCar",
        "1577-Steampunk",
        "1580-The Blue Monkeys",
        "1657-Hamosad",
        "1690-Orbit",
        "1937-Elysium",
        "1942-Cyber Knights",
        "1954-Alephbots",
        "2096-RoboActive",
        "2212-The Spikes",
        "2230-Ziboti",
        "2630-Thunderbolts",
        "2679-Robytes",
        "3075-Ha-Dream Team",
        "3083-FTA",
        "3211-The Y Team",
        "3339-BumbleB",
        "3388-Flash",
        "3835-Magical Unicorns",
        "4320-The Joker",
        "4338-Falcons",
        "4515-Orbit-CB",
        "4590-GreenBlitz",
        "4599-Mighty Tech",
        "4661-Shachar",
        "4744-Ninjas",
        "5291-Tzahala",
        "5292-Segev",
        "5554-The Poros",
        "5635-Demacia",
        "5654-Phenix",
        "5747-PIbots",
        "5951-Toro",
        "5987-Galaxia",
        "6168-Alphabots",
        "6738-Excalibur",
        "6740-G3",
        "7039-X-SHADOVV",
        "7067-Teaspoon",
        "7157-Raminators",
        "7290-Infinity",
        "7845-The Galilego",
        "8175-Astromechs",
        "8215-HaHish Team",
        "8223-Pixel",
        "8325-Metallic Raptors",
    ]


class DynamicVariables:

    inputText = None

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

    # Set transparency levels
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
