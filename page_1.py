from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyFirstApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.label = Label(text="Welcome to Kivy!")
        self.add_widget(self.label)

        self.text_input = TextInput(hint_text="Type something...", multiline=False)
        self.add_widget(self.text_input)

        self.button = Button(text="Update Label")
        self.button.bind(on_press=self.update_label)
        self.add_widget(self.button)

    def update_label(self, instance):
        self.label.text = f"You typed: {self.text_input.text}"

class MainApp(App):
    def build(self):
        return MyFirstApp()

if __name__ == "__main__":
    MainApp().run()
