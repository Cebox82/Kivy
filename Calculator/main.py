from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CalculatorLayout(BoxLayout):
    def clear(self):
        self.ids.result_label.text = ''

    def calculate(self):
        try:
            expression = self.ids.result_label.text
            result = eval(expression)
            self.ids.result_label.text = str(result)
        except Exception as e:
            self.ids.result_label.text = 'error'

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    CalculatorApp().run()