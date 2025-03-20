from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout

class DistanceTraveledApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Label asking for speed input
        self.label1 = Label(text="Enter the car's speed (miles per hour):")
        self.layout.add_widget(self.label1)

        # Text input for speed
        self.speed_input = TextInput(multiline=False, input_filter='float', size_hint=(None, None), width=200)
        self.layout.add_widget(self.speed_input)

        # Buttons for each time (5, 8, and 12 hours)
        self.button_5_hours = Button(text="Calculate Distance for 5 hours")
        self.button_5_hours.bind(on_press=self.calculate_distance_5)
        self.layout.add_widget(self.button_5_hours)

        self.button_8_hours = Button(text="Calculate Distance for 8 hours")
        self.button_8_hours.bind(on_press=self.calculate_distance_8)
        self.layout.add_widget(self.button_8_hours)

        self.button_12_hours = Button(text="Calculate Distance for 12 hours")
        self.button_12_hours.bind(on_press=self.calculate_distance_12)
        self.layout.add_widget(self.button_12_hours)

        # Result label
        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        # "Desmond Brown" at the bottom left
        self.anchor = AnchorLayout(anchor_x='left', anchor_y='bottom')
        self.footer_label = Label(text="Desmond Brown", size_hint=(None, None), size=(200, 50))
        self.anchor.add_widget(self.footer_label)
        self.layout.add_widget(self.anchor)

        return self.layout

    # Function for calculating distance at 5 hours
    def calculate_distance_5(self, instance):
        self.calculate_distance(5)

    # Function for calculating distance at 8 hours
    def calculate_distance_8(self, instance):
        self.calculate_distance(8)

    # Function for calculating distance at 12 hours
    def calculate_distance_12(self, instance):
        self.calculate_distance(12)

    # Helper function to calculate and display the distance
    def calculate_distance(self, time):
        try:
            speed = float(self.speed_input.text)
            distance = speed * time
            self.result_label.text = f"The distance the car will travel in {time} hours: {distance} miles."
        except ValueError:
            self.result_label.text = "Please enter a valid number for speed."

if __name__ == '__main__':
    DistanceTraveledApp().run()