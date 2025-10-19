
from kivymd.uix.button import MDButton, MDButtonText
from kivy.metrics import dp
from datetime import datetime, timedelta
from kivymd.uix.boxlayout import MDBoxLayout

class CalendarStrip(MDBoxLayout):
    def __init__(self, days_count=6, **kwargs):
        super().__init__(orientation="horizontal", spacing=dp(8), padding=dp(8), **kwargs)

        today = datetime.now()

        for i in range(days_count):
            day = today + timedelta(days=i)
            text = day.strftime("%d.%m")

            # Создаём кнопку
            btn = MDButton(
                style="outlined",
                height=dp(40),
                size_hint=(None, None),
                width=dp(80),
            )

            # Добавляем текст
            btn_text = MDButtonText(text=text)
            btn.add_widget(btn_text)


            # Подсвечиваем сегодняшний день
            if i == 0:
                btn.style = "tonal"



            self.add_widget(btn)





