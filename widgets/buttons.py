import customtkinter

from config import Config


conf = Config()

IS_ANSWER = False


def clean_output_area(output_field:customtkinter.CTkTextbox):
    output_field.delete('0.0', 'end')


class Button(customtkinter.CTkButton):
    def __init__(self,
        master,
        text,
        output_field:customtkinter.CTkTextbox,
        font=conf.FONT,
        fg_color=conf.FG_COLOR_BUTTON,
        hover_color=conf.HOVER_COLOR_BUTTON,
        corner_radius=conf.CORNER_RADIUS):

        self.text = text
        self.width = master.winfo_screenwidth()
        self.height = conf.DEFAULT_BUTTON_HEIGHT
        self._command = lambda output_field=output_field: self.command(output_field)
        
        super().__init__(
            master=master,
            text=self.text,
            width=self.width,
            height=self.height,
            font=font,
            fg_color=fg_color,
            hover_color=hover_color,
            corner_radius=corner_radius,
            command=self._command
        )

    def command(self, output_field:customtkinter.CTkTextbox):
        global IS_ANSWER
        data = output_field.get('0.0', 'end')
        
        if data.startswith('division by zero') or data.startswith('invalid syntax') or \
            IS_ANSWER and (self.text.isdigit() or self.text == '.'):
            clean_output_area(output_field)

        output_field.insert('end', self.text)
        IS_ANSWER = False


class FieldCearingButton(Button):
    def __init__(self, master, text, output_field:customtkinter.CTkTextbox):

        self._command = lambda output_field=output_field: self.command(output_field)

        super().__init__(
            master=master,
            text=text,
            output_field=output_field,
        )

    def command(self, output_field:customtkinter.CTkTextbox):
        clean_output_area(output_field)


class SymbolDeletionButton(Button):
    def __init__(self, master, text, output_field:customtkinter.CTkTextbox):
        self._command = lambda output_field=output_field: self.command(output_field)

        super().__init__(
            master=master,
            text=text,
            output_field=output_field,
        )

    def command(self, output_field:customtkinter.CTkTextbox):
        data = output_field.get('0.0', 'end')[:-1]
        clean_output_area(output_field)

        if data.startswith('division by zero') or data.startswith('invalid syntax') or IS_ANSWER:
            output_field.insert('0.0', '')
        else:
            output_field.insert('0.0', data[:-1])


class DigitButton(Button):
    def __init__(self, master, text, output_field:customtkinter.CTkTextbox):
        self._fg_color = conf.DIGIT_FG_COLOR_BUTTON
        self._hover_color = conf.DIGIT_HOVER_COLOR_BUTTON
        
        super().__init__(
            master=master,
            text=text,
            output_field=output_field,
            fg_color=self._fg_color,
            hover_color=self._hover_color
        )


class CalculationButton(Button):
    def __init__(self, master, text, output_field:customtkinter.CTkTextbox):

        self._fg_color = conf.FG_COLOR_CALCULATION_BUTTON
        self._hover_color = conf.HOVER_COLOR_CALCULATION_BUTTON
        self._command = lambda output_field=output_field: self.command(output_field)

        super().__init__(
            master=master,
            text=text,
            output_field=output_field,
            fg_color=self._fg_color,
            hover_color=self._hover_color
        )

    def command(self, output_field:customtkinter.CTkTextbox):
        """ calculation """
        global IS_ANSWER

        data = output_field.get('0.0', 'end').replace('^', '**').replace('x', '*')
        clean_output_area(output_field)

        while data.startswith('0'):
            data = data.replace('0', '', 1)

        try:
            result = f'{eval(data)}'
            output_field.insert('0.0', result)
            IS_ANSWER = True

        except ZeroDivisionError:
            output_field.insert('0.0', 'division by zero')
        
        except SyntaxError:
            output_field.insert('0.0', 'invalid syntax')


