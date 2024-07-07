from kivy.lang import Builder

KV = """
<HomeScreen>:
    name: 'home'
    MDRectangleFlatButton:
        text: 'Start new scouting trip'
        text_color: 0, 0, 0, 1
        md_bg_color: 1, 0, 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.07}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'autonomous_period'
    Image:
        source: "Sources/FRC_fild_Image.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        size_hint: 0.95, 1
    Image:
        source: "Sources/grop_logo.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.77}
        size_hint: 0.95, 1
"""

Builder.load_string(KV)