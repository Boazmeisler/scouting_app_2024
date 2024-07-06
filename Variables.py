class Constants():
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

class DynamicVariables():

    inputText = None

    isDefend = False
    isGetDefended = False
    isNether = False

    isDidntTry = 0
    isTriedAndFail = 0
    isClimbAlone = 0
    isClimbInHarmony = 0
    isTrapAlone = 0
    isTrapInHarmony = 0


    # Set transparency levels
    stage_note_transparency = 0.1
    speaker_note_transparency = 0.1
    amp_note_transparency = 0.1
    mid_field_lowest_note_transparency = 0.1
    mid_field_low_note_transparency = 0.1
    mid_field_mid_note_transparency = 0.1
    mid_field_high_note_transparency = 0.1
    mid_field_highest_note_transparency = 0.1
    A_area_transparency = 0.1
    B_area_transparency = 0.1
    C_area_transparency = 0.1
    D_area_transparency = 0.1


    auto_amp_count = "0"
    auto_missed = "0"
    robot_Passed_the_Line = None
    teleop_speaker_scored_count = "0"
    teleop_amp_scored_count = "0"
    teleop_speaker_missed_count = "0"
    teleop_amp_missed_count = "0"
    teleop_delivery_count = "0"
        
    teleop_current_display_stats = "scored: 0" + "\n" + "missed: 0"