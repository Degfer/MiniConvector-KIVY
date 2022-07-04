from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Convector"

class MyConvectorApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='My program\nEverything is working!')
        self.miles = Label(text='Miles')
        self.meters = Label(text='Meters')
        self.centimeters = Label(text='Centimeters')
        self.input_data = TextInput(hint_text='Enter value (km)', multiline=False)
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.miles.text = 'Miles: ' + str(float(data) * 0.62)
            self.meters.text = 'Meters: ' + str(float(data) * 1000)
            self.centimeters.text = 'Centimeters: ' + str(float(data) * 100000)
        else:
            self.input_data.text = ''

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.miles)
        box.add_widget(self.meters)
        box.add_widget(self.centimeters)

        return box

if __name__ == "__main__":
    MyConvectorApp().run()