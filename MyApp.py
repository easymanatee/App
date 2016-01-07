import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox

class Apps1(App):
    icon = "vrreality-Logo1.0.png"

    def build(self):
        #self.title = "VR Reality News"
        return FloatLayout()
        
    
    


if __name__ == "__main__":
    Apps1().run()
