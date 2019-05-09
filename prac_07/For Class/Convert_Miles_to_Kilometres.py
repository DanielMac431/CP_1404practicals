from kivy.app import App
from kivy.lang import Builder

CONVERSION_CONSTANT = 1.60934
class DistanceConversion(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('Convert Milest to Kilometres.kv')
        return self.root

    def handle_increment(self, user_input, increment):
        number = self.input_check(user_input) + increment
        self.root.ids.input_number.text = str(number)


    def handle_convert(self, value):
        result = self.input_check(value) * CONVERSION_CONSTANT
        self.root.ids.output_label.text = str(result)

    def input_check(self, text):
        try:
            input_number = float(text)
            return input_number
        except ValueError:
            return 0.0

DistanceConversion().run()
    # class BoxLayoutDemo(App):
    #     def build(self):
    #         self.title = "Box Layout Demo"
    #         self.root = Builder.load_file('box_layout.kv')
    #         return self.root
    #
    #     def handle_greet(self):
    #         self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text
    #
    #     def clear(self):
    #         self.root.ids.output_label.text = ''
    #         self.root.ids.input_name.text = ''
