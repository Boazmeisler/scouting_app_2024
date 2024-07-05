KV = """
<TeleopEndGamePeriod>:
    name: 'end'
    MDLabel:
        text: "Click on what happened in the game"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        halign: "center"
        font_size: "17sp"

    MDBoxLayout:
        id: DidntTry
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        size_hint: 0.9, None
        size: [0,70]
        md_bg_color: 1, 0, 0, 1
        radius: 5
        MDLabel:
            text: "Didn't try to climb"
            halign: 'center'
            font_size: "25sp"
            pos_hint: {'center_x': 0.7, 'center_y': 0.5}
            color: 1, 1, 1, 1

    MDBoxLayout:
        id: TriedAndFail
        pos_hint: {'center_x': 0.5, 'center_y': 0.67}
        size_hint: 0.9, None
        size: [0,70]
        md_bg_color: 1, 0, 0, 1
        radius: 5
        MDLabel:
            text: "Tried to climb but failed"
            halign: 'center'
            font_size: "25sp"
            pos_hint: {'center_x': 0.7, 'center_y': 0.5}
            color: 1, 1, 1, 1

    MDBoxLayout:
        id: ClimbAlone
        pos_hint: {'center_x': 0.5, 'center_y': 0.54}
        size_hint: 0.9, None
        size: [0,70]
        md_bg_color: 1, 0, 0, 1
        radius: 5
        MDLabel:
            text: "Climb alone"
            halign: 'center'
            font_size: "25sp"
            pos_hint: {'center_x': 0.7, 'center_y': 0.5}
            color: 1, 1, 1, 1

    MDBoxLayout:
        id: ClimbInHarmony
        pos_hint: {'center_x': 0.5, 'center_y': 0.41}
        size_hint: 0.9, None
        size: [0,70]
        md_bg_color: 1, 0, 0, 1
        radius: 5
        MDLabel:
            text: "Climb in harmony"
            halign: 'center'
            font_size: "25sp"
            pos_hint: {'center_x': 0.7, 'center_y': 0.5}
            color: 1, 1, 1, 1

    MDBoxLayout:
        id: TrapAlone
        pos_hint: {'center_x': 0.5, 'center_y': 0.28}
        size_hint: 0.9, None
        size: [0,70]
        md_bg_color: 1, 0, 0, 1
        radius: 5
        MDLabel:
            text: "Trap alone"
            halign: 'center'
            font_size: "25sp"
            pos_hint: {'center_x': 0.7, 'center_y': 0.5}
            color: 1, 1, 1, 1

    MDBoxLayout:
        id: TrapInHarmony
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        size_hint: 0.9, None
        size: [0,70]
        md_bg_color: 1, 0, 0, 1
        radius: 5
        MDLabel:
            text: "Trap in harmony"
            halign: 'center'
            font_size: "25sp"
            pos_hint: {'center_x': 0.7, 'center_y': 0.5}
            color: 1, 1, 1, 1

    MDRectangleFlatButton:
        md_bg_color: 0, 0, 0, 0
        text: ""
        size_hint: 0.9, None
        size: [0,70]
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        on_press:
            app.endGameButtonFunctionality(DidntTry)

    MDRectangleFlatButton:
        md_bg_color: 0, 0, 0, 0
        text: ""
        size_hint: 0.9, None
        size: [0,70]
        pos_hint: {'center_x': 0.5, 'center_y': 0.67}
        on_press:
            app.endGameButtonFunctionality(TriedAndFail)

    MDRectangleFlatButton:
        md_bg_color: 0, 0, 0, 0
        text: ""
        size_hint: 0.9, None
        size: [0,70]
        pos_hint: {'center_x': 0.5, 'center_y': 0.54}
        on_press:
            app.endGameButtonFunctionality(ClimbAlone)

    MDRectangleFlatButton:
        md_bg_color: 0, 0, 0, 0
        text: ""
        size_hint: 0.9, None
        size: [0,70]
        pos_hint: {'center_x': 0.5, 'center_y': 0.41}
        on_press:
            app.endGameButtonFunctionality(ClimbInHarmony)

    MDRectangleFlatButton:
        md_bg_color: 0, 0, 0, 0
        text: ""
        size_hint: 0.9, None
        size: [0,70]
        pos_hint: {'center_x': 0.5, 'center_y': 0.28}
        on_press:
            app.endGameButtonFunctionality(TrapAlone)

    MDRectangleFlatButton:
        md_bg_color: 0, 0, 0, 0
        text: ""
        size_hint: 0.9, None
        size: [0,70]
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
          #  root.manager.current = 'end'

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