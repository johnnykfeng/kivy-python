from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from calculator_backend import Calculator

# Set window size and background color
Window.size = (400, 600)
Window.clearcolor = (0.95, 0.95, 0.95, 1)  # Light gray background


class StyledButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.2, 0.6, 0.8, 1)  # Blue color
        self.color = (1, 1, 1, 1)  # White text
        self.font_size = '24sp'
        self.bold = True
        self.size_hint = (1, 1)
        self.border = (0, 0, 0, 0)


class OperationButton(StyledButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.8, 0.4, 0.2, 1)  # Orange color


class EqualsButton(StyledButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.2, 0.8, 0.4, 1)  # Green color


class ClearButton(StyledButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.8, 0.2, 0.2, 1)  # Red color


class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Add a title
        title = Label(
            text='Calculator',
            font_size='32sp',
            bold=True,
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=0.15
        )
        self.add_widget(title)

        # Display
        self.display = TextInput(
            multiline=False,
            readonly=True,
            font_size=40,
            size_hint_y=0.2,
            background_color=(1, 1, 1, 1),
            foreground_color=(0.2, 0.2, 0.2, 1),
            cursor_color=(0.2, 0.2, 0.2, 1),
            padding=[10, 10],
            background_normal='',
            background_active=''
        )
        self.add_widget(self.display)

        # Buttons layout
        buttons_layout = BoxLayout(orientation='vertical', spacing=10)

        # First row - Numbers 7-9 and divide
        row1 = BoxLayout(spacing=10)
        for num in ['7', '8', '9']:
            btn = StyledButton(text=num, on_press=self.on_button_press)
            row1.add_widget(btn)
        btn = OperationButton(text='/', on_press=self.on_button_press)
        row1.add_widget(btn)
        buttons_layout.add_widget(row1)

        # Second row - Numbers 4-6 and multiply
        row2 = BoxLayout(spacing=10)
        for num in ['4', '5', '6']:
            btn = StyledButton(text=num, on_press=self.on_button_press)
            row2.add_widget(btn)
        btn = OperationButton(text='*', on_press=self.on_button_press)
        row2.add_widget(btn)
        buttons_layout.add_widget(row2)

        # Third row - Numbers 1-3 and subtract
        row3 = BoxLayout(spacing=10)
        for num in ['1', '2', '3']:
            btn = StyledButton(text=num, on_press=self.on_button_press)
            row3.add_widget(btn)
        btn = OperationButton(text='-', on_press=self.on_button_press)
        row3.add_widget(btn)
        buttons_layout.add_widget(row3)

        # Fourth row - 0, clear, equals, and add
        row4 = BoxLayout(spacing=10)
        btn = StyledButton(text='0', on_press=self.on_button_press)
        row4.add_widget(btn)
        btn = ClearButton(text='C', on_press=self.on_button_press)
        row4.add_widget(btn)
        btn = EqualsButton(text='=', on_press=self.on_button_press)
        row4.add_widget(btn)
        btn = OperationButton(text='+', on_press=self.on_button_press)
        row4.add_widget(btn)
        buttons_layout.add_widget(row4)

        self.add_widget(buttons_layout)

        # Initialize calculator state
        self.current_number = ''
        self.first_number = None
        self.operation = None

    def on_button_press(self, instance):
        text = instance.text

        if text == 'C':
            self.clear()
        elif text == '=':
            self.calculate_result()
        elif text in ['+', '-', '*', '/']:
            self.handle_operation(text)
        else:
            self.current_number += text
            self.update_display()

    def clear(self):
        self.current_number = ''
        self.first_number = None
        self.operation = None
        self.display.text = ''

    def handle_operation(self, op):
        if self.current_number:
            if self.first_number is None:
                self.first_number = float(self.current_number)
            else:
                self.calculate_result()
            self.operation = op
            self.current_number = ''

    def calculate_result(self):
        if self.first_number is not None and self.operation and self.current_number:
            result = Calculator.calculate(
                self.operation,
                self.first_number,
                float(self.current_number)
            )
            self.display.text = str(result)
            self.first_number = result
            self.current_number = ''
            self.operation = None

    def update_display(self):
        self.display.text = self.current_number


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    CalculatorApp().run()
