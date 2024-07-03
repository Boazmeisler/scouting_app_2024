KV = """
<TeleopMidGamePeriod>:
    name: 'teleop_mid'
#----------------------------------********speaker********---------------------------------------
    Image:
        source: "Sources/speaker_POV.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.83}
        size_hint: 0.89, 0.3
        allow_stretch: True
        keep_ratio: False
    Image:
        source: "Sources/Target_icon.png"
        size_hint: None, None
        size: [35,35]
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
    MDRoundFlatButton: #scored button
        text: ''
        md_bg_color: 1, 0, 1, 0
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        size_hint: None, None
        size: [35,35]
        on_press: app.addition(speaker_current_situation,"teleop_speaker_scored")
    Image:
        source: "Sources/X_icon.png"
        size_hint: None, None
        size: [35,35]
        pos_hint: {'center_x': 0.2, 'center_y': 0.9}
    MDRoundFlatButton: #missed button
        text: ''
        md_bg_color: 1, 0, 1, 0
        pos_hint: {'center_x': 0.2, 'center_y': 0.9}
        size_hint: None, None
        size: [35,35]
        on_press: app.addition(speaker_current_situation,"teleop_speaker_missed")

    MDLabel:
        id: speaker_current_situation
        text: app.teleop_current_display_stats
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.8,'center_y': 0.94}
        halign: "center"
#----------------------------------********speaker********---------------------------------------
    Image:
        source: "Sources/AMP_POV.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: 0.9, 0.3
        allow_stretch: True
        keep_ratio: False
    Image:
        source: "Sources/Target_icon.png"
        size_hint: None, None
        size: [35,35]
        pos_hint: {'center_x': 0.51, 'center_y': 0.5}
    MDRoundFlatButton: #scored button
        text: ''
        md_bg_color: 1, 0, 1, 0
        pos_hint: {'center_x': 0.51, 'center_y': 0.5}
        size_hint: None, None
        size: [35,35]
        on_press: app.addition(amp_current_situation,"teleop_amp_scored")
    Image:
        source: "Sources/X_icon.png"
        size_hint: None, None
        size: [35,35]
        pos_hint: {'center_x': 0.15, 'center_y': 0.6}
    MDRoundFlatButton: #missed button
        text: ''
        md_bg_color: 1, 0, 1, 0
        pos_hint: {'center_x': 0.15, 'center_y': 0.6}
        size_hint: None, None
        size: [35,35]
        on_press: app.addition(amp_current_situation,"teleop_amp_missed")
    MDLabel:
        id: amp_current_situation
        text: app.teleop_current_display_stats
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.8,'center_y': 0.6}
        halign: "center"
#----------------------------------******delivery******----------------------------------
    MDLabel:
        text: "How much did the robot delivery:"
        color: 1, 1, 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        padding: 15
        font_size: "17sp"
        halign: "center"

    MDFloatingActionButton: # add button
        icon: "plus"
        pos_hint: {'center_x': 0.85, 'center_y': 0.17}
        md_bg_color: 0, 1, 0, 1
        on_press: app.addition(delivery_display, "teleop_delivery_add")  

    MDFloatingActionButton: # subtract button
        icon: "minus"
        md_bg_color: 1, 0, 0, 1
        pos_hint: {'center_x': 0.15, 'center_y': 0.17}
        on_press: app.subtract(delivery_display, 'teleop_delivery_subtract')


    MDBoxLayout:
        pos_hint: {'center_x': 0.5, 'center_y': 0.17}
        size_hint: 0.48, 0.08
        md_bg_color: 1, 1, 1, 1
        radius: 20
        MDLabel:
            id: delivery_display
            text: app.teleop_delivery_count
            halign: 'center'
            font_size: "40sp"
            pos_hint: {'center_x': 0.7, 'center_y': 0.5}
            color: 0, 0, 0, 1

        # Next button
    MDRectangleFlatButton:
        pos_hint: {'center_x': 0.85, 'center_y': 0.05}
        text: "Next"
        md_bg_color: 0, 0, 1, 1
        text_color: 1, 1, 1, 1
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'end'
        # Back button
    MDRectangleFlatButton:
        pos_hint: {'center_x': 0.15, 'center_y': 0.05}
        text: "Back"
        md_bg_color: 1, 0, 0, 1
        text_color: 1, 1, 1, 1
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = 'autonomous_period'
        """
