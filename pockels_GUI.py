from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder


class PockelsRoot(FloatLayout):
    pass


class PockelsApp(App):
    def build(self):
        Builder.load_file('pockels_GUI.kv')
        return PockelsRoot()


if __name__ == '__main__':
    PockelsApp().run()
