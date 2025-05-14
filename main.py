from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import subprocess
import sys
import os

class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)

        # Title
        self.add_widget(Button(
            text='Welcome to the Demo App',
            size_hint_y=0.2,
            background_color=(0.2, 0.6, 1, 1),
            disabled=True
        ))

        # Navigation Buttons
        self.page1_btn = Button(
            text='Go to Basic Demo (Page 1)',
            size_hint_y=0.4,
            background_color=(0.3, 0.7, 0.3, 1)
        )
        self.page1_btn.bind(on_press=self.open_page1)
        self.add_widget(self.page1_btn)

        self.page2_btn = Button(
            text='Go to Form Demo (Page 2)',
            size_hint_y=0.4,
            background_color=(0.7, 0.3, 0.3, 1)
        )
        self.page2_btn.bind(on_press=self.open_page2)
        self.add_widget(self.page2_btn)

        self.page3_btn = Button(
            text='Go to Calculator Demo (Page 3)',
            size_hint_y=0.4,
            background_color=(0.4, 0.3, 0.7, 1)
        )
        self.page3_btn.bind(on_press=self.open_page3)
        self.add_widget(self.page3_btn)


    def open_page1(self, instance):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_dir, 'page_1.py')
        App.get_running_app().stop()
        subprocess.Popen([sys.executable, script_path])

    def open_page2(self, instance):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_dir, 'page_2.py')
        App.get_running_app().stop()
        subprocess.Popen([sys.executable, script_path])
        
    def open_page3(self, instance):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_dir, 'calculator_page.py')
        App.get_running_app().stop()
        subprocess.Popen([sys.executable, script_path])

class MainApp(App):
    def build(self):
        return HomePage()

if __name__ == "__main__":
    MainApp().run()
