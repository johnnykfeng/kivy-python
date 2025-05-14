from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout


class CommaNumberInput(TextInput):
    """
    A custom TextInput widget that only accepts comma-separated numbers.
    
    This widget extends TextInput to create a specialized input field that:
    - Only allows numbers and commas to be entered
    - Is single-line (multiline=False) 
    - Shows hint text explaining the expected format
    - Validates input to ensure only valid characters are entered
    
    Example usage:
        comma_input = CommaNumberInput()
        # User can enter: "1,2,3,4"
        # User cannot enter: "abc" or special characters
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiline = False
        self.hint_text = "Enter numbers separated by commas (e.g., 1,2,3,4)"

    def insert_text(self, substring, from_undo=False):
        # Only allow numbers and commas
        if substring == ',' or substring.isdigit():
            return super().insert_text(substring, from_undo=from_undo)
        return False


class MyForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        # Text Input
        self.text_input = TextInput(hint_text="Enter text here")
        self.add_widget(Label(text="Text Input:"))
        self.add_widget(self.text_input)

        # Number Input
        self.number_input = TextInput(
            hint_text="Enter a number", input_filter='int')
        self.add_widget(Label(text="Number Input:"))
        self.add_widget(self.number_input)

        # Comma-separated Numbers Input
        self.comma_numbers_input = CommaNumberInput()
        self.add_widget(Label(text="Comma-separated Numbers:"))
        self.add_widget(self.comma_numbers_input)

        # Dropdown (Spinner)
        self.dropdown = Spinner(
            text='Select an option',
            values=('Option 1', 'Option 2', 'Option 3')
        )
        self.add_widget(Label(text="Dropdown:"))
        self.add_widget(self.dropdown)

        # Radio Buttons
        self.add_widget(Label(text="Choose one:"))
        self.radio_layout = GridLayout(cols=3, size_hint_y=None, height=40)
        self.radio1 = ToggleButton(
            text="Choice A", group="radio", state='down')
        self.radio2 = ToggleButton(text="Choice B", group="radio")
        self.radio3 = ToggleButton(text="Choice C", group="radio")
        self.radio_layout.add_widget(self.radio1)
        self.radio_layout.add_widget(self.radio2)
        self.radio_layout.add_widget(self.radio3)
        self.add_widget(self.radio_layout)

        # Submit Button
        self.submit_btn = Button(text="Submit")
        self.submit_btn.bind(on_press=self.print_values)
        self.add_widget(self.submit_btn)

    def print_values(self, instance):
        text_val = self.text_input.text
        number_val = self.number_input.text
        comma_numbers = self.comma_numbers_input.text
        dropdown_val = self.dropdown.text
        radio_val = None
        for radio in [self.radio1, self.radio2, self.radio3]:
            if radio.state == 'down':
                radio_val = radio.text
                break

        print("Text Input:", text_val)
        print("Number Input:", number_val)
        # print("Comma-separated Numbers:", comma_numbers)
        comma_numbers_list = [int(num.strip()) for num in comma_numbers.split(',') if num.strip()]
        
        print("Comma-separated Numbers (as list):", comma_numbers_list)
        print("Dropdown Selection:", dropdown_val)
        print("Radio Selection:", radio_val)


class MyApp(App):
    def build(self):
        return MyForm()


if __name__ == "__main__":
    MyApp().run()
