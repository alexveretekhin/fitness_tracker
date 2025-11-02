
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.pickers import MDDockedDatePicker



Window.size = (350, 600)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("kv/components/calendar.kv")

    def show_date_picker(self):
        date_dialog = MDDockedDatePicker()
        date_dialog.bind(on_save=self.on_save_date)
        date_dialog.open()

    def on_save_date(self, instance, value, date_range):
        print(f"Выбранная дата: {value}")

if __name__ == "__main__":
    MainApp().run()
