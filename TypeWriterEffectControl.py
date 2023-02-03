import flet as ft
import time


class TypeWriterControl(ft.UserControl):
    def __init__(self, value="", font_family="SourceCodePro-BlackItalic", color="#ffffff", transparency=True):
        super().__init__()
        self.text_to_print = str(value)
        self.font_family = font_family
        self.text_color = color
        self.transparency = transparency

    def did_mount(self):
        self.effect()

    def update(self):
        super().update()
        self.effect()

    def effect(self):
        self.my_type_writter_text.value = ""
        for i in range(len(self.text_to_print)):
            self.my_type_writter_text.value += self.text_to_print[i] + "_"
            self.my_type_writter_text.font_family = self.font_family
            self.my_type_writter_text.color = self.text_color
            self.my_type_writter_text.opacity = 1 if self.transparency == True else 0
            self.my_type_writter_text.update()
            self.my_type_writter_text.value = self.my_type_writter_text.value[:-1]
            time.sleep(0.06)
        self.my_type_writter_text.update()
    
    def build(self):
        self.my_type_writter_text = ft.Text(value="", no_wrap=False)
        return self.my_type_writter_text