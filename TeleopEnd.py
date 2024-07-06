KV = """
<TeleopEndGamePeriod>:
    name: 'end'
    MDLabel:
        text: "Click on what happened in the game"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        halign: "center"
        font_size: "17sp"


    MDRectangleFlatButton:
        id: DidntTry
        md_bg_color: 1, 0, 0, 1
        text: "Didn't try to climb"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        on_press:
            app.endGameButtonFunctionality(DidntTry)

    MDRectangleFlatButton:
        id: TriedAndFail
        md_bg_color: 1, 0, 0, 1
        text: "Tried but failed"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.67}
        on_press:
            app.endGameButtonFunctionality(TriedAndFail)

    MDRectangleFlatButton:
        id: ClimbAlone
        md_bg_color: 1, 0, 0, 1
        text: "Climb alone"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.54}
        on_press:
            app.endGameButtonFunctionality(ClimbAlone)

    MDRectangleFlatButton:
        id: ClimbInHarmony
        md_bg_color: 1, 0, 0, 1
        text: "Climb in harmony"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.41}
        on_press:
            app.endGameButtonFunctionality(ClimbInHarmony)

    MDRectangleFlatButton:
        id: TrapAlone
        md_bg_color: 1, 0, 0, 1
        text: "Trap alone"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.28}
        on_press:
            app.endGameButtonFunctionality(TrapAlone)

    MDRectangleFlatButton:
        id: TrapInHarmony
        md_bg_color: 1, 0, 0, 1
        text: "Trap in harmony"
        size_hint: 0.9, None
        size: [0,70]
        font_size: "25sp"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        on_press:
            app.endGameButtonFunctionality(TrapInHarmony)

    # Next button
    MDRectangleFlatButton:
        pos_hint: {'center_x': 0.85, 'center_y': 0.05}
        text: "Next"
        md_bg_color: 0, 0, 1, 1
        text_color: 1, 1, 1, 1
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'general'

        # Back button
    MDRectangleFlatButton:
        pos_hint: {'center_x': 0.15, 'center_y': 0.05}
        text: "Back"
        md_bg_color: 1, 0, 0, 1
        text_color: 1, 1, 1, 1
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = 'teleop_mid'


"""