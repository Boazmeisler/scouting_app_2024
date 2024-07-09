from kivy.lang import Builder

KV = """
<PreScouting>:
    name: "preScout"
    MDLabel:
        text: "your name"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5,'center_y': 0.9}
        halign: "center"
    MDTextField:
        id: scouter_name
        font_name: "Arial"
        md_bg_color: 1,1,1,1
        halign: "center"
        hint_text: "write here"
        pos_hint:{'center_x': 0.5, 'center_y': 0.83}
        size_hint_x:0.9
    MDLabel:
        text: "group_num"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5,'center_y': 0.7}
        halign: "center"
    Spinner:
        id: group_num
        text: 'Select an option'
        pos_hint: {'center_x': 0.5,'center_y': 0.58}
        values: app.teams
        size_hint: 0.9, None
        size: 200, 70
    MDLabel:
        text: "qualification game number"
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5,'center_y': 0.4}
        halign: "center"
    MDTextField:
        id: qualification_num
        font_name: "Arial"
        md_bg_color: 1,1,1,1
        halign: "center"
        hint_text: "write here"
        pos_hint:{'center_x': 0.5, 'center_y': 0.33}
        size_hint_x:0.9
    # Next button
    MDRectangleFlatButton:
        pos_hint: {'center_x': 0.85, 'center_y': 0.05}
        text: "Next"
        md_bg_color: 0, 0, 1, 1
        text_color: 1, 1, 1, 1
        on_press:
            root.manager.transition.direction = 'left'
            app.rememberPreScout()
            root.manager.current = 'autonomous_period'
"""

Builder.load_string(KV)
