"""
CP1404 Practical
Dynamic Kivy Widgets
17/11/2024
Harrison O'Kane
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicNamesApp(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Names"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from dictionary entries and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


if __name__ == '__main__':
    DynamicNamesApp().run()