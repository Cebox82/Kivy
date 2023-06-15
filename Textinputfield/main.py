from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


class ConsoleOutputLayout(BoxLayout):
    def print_text(self):
        text = self.ids.text_input.text
        print(text)

class ConsoleOutputApp(App):
    def build(self):
        Window.size = (400,300)
        return ConsoleOutputLayout()


if __name__ == '__main__':
    ConsoleOutputApp().run()