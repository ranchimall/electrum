from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty

Builder.load_string('''
<FLODataDialog@Popup>
    id: popup
    title: ''
    size_hint: 0.8, 0.5
    pos_hint: {'top':0.9}
    BoxLayout:
        orientation: 'vertical'
        Widget:
            size_hint: 1, 0.1
        LimitedInput:
            id:input
            padding: '5dp'
            size_hint: 1, 1
            height: '27dp'
            max_characters: 1022
            pos_hint: {'center_y':.5}
            text:''
            multiline: True
            background_normal: 'atlas://electrum/gui/kivy/theming/light/tab_btn'
            background_active: 'atlas://electrum/gui/kivy/theming/light/tab_btn'
            hint_text_color: self.foreground_color
            foreground_color: 1, 1, 1, 1
            font_size: '16dp'
            focus: True
        Widget:
            size_hint: 1, 0.2
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.5
            Button:
                text: 'Cancel'
                size_hint: 0.5, None
                height: '48dp'
                on_release: popup.dismiss()
            Button:
                text: 'OK'
                size_hint: 0.5, None
                height: '48dp'
                on_release:
                    root.callback(input.text)
                    popup.dismiss()
''')

class LimitedInput(TextInput):
    max_characters = NumericProperty(0)
    def insert_text(self, substring, from_undo=False):
        if len(self.text) > self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)

class FLODataDialog(Factory.Popup):

    def __init__(self, title, text, callback):
        Factory.Popup.__init__(self)
        self.ids.input.text = text
        self.callback = callback
        self.title = title
