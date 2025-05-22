from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

# Set default window size
Window.size = (1200, 700)


class PockelsRoot(FloatLayout):
    def preview_routine(self):
        ids = self.ids
        # Collect all left column input values
        values = {
            'Save Folder': ids.save_folder_input.text,
            'Part ID': ids.part_id_input.text,
            'Trial #': ids.trial_num_input.text,
            '1550nm LED Current': ids.led_current_input.text,
            'Analyzer Parallel': ids.analyzer_parallel_input.text,
            'Analyzer Cross': ids.analyzer_cross_input.text,
            'Voltage Sweep Start': ids.voltage_start_input.text,
            'Voltage Sweep Stop': ids.voltage_stop_input.text,
            'Voltage Sweep Step': ids.voltage_step_input.text,
            'X-ray Sweep': ids.xray_sweep_input.text,
            'Red LED Sweep': ids.red_led_sweep_input.text,
        }
        # Format the output
        output = 'Input Numbers:\n'
        for k, v in values.items():
            output += f'{k}: {v}\n'
        self.ids.routine_output_label.text = output
        print(f"Previewing routine with input numbers: {values}")
        print(f"Output: {output}")


class PockelsApp(App):
    def build(self):
        Builder.load_file('pockels_GUI.kv')
        return PockelsRoot()


if __name__ == '__main__':
    PockelsApp().run()
