import customtkinter

from config import Config

from widgets.output_field import OutputFiled
from widgets.buttons import *


conf = Config()


class Calculator(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title = conf.TITLE
        self.geometry(f'{conf.WINDOW_SIZE[0]}x{conf.WINDOW_SIZE[1]}')
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        self.output_field = OutputFiled(master=self)
        self.output_field.grid(row=0, column=0, columnspan=4, pady=5, padx=5)
        
        self.create_buttons()

    def create_buttons(self):
        for i in range(len(conf.BUTTONS_TEXT)):
            for j in range(len(conf.BUTTONS_TEXT[i])):

                button_text = conf.BUTTONS_TEXT[i][j]

                match button_text:
                    case 'C':
                        self.button = FieldCearingButton(
                            master=self,
                            text=button_text,
                            output_field=self.output_field
                        )

                    case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '0':
                        self.button = DigitButton(
                            master=self,
                            text=button_text,
                            output_field=self.output_field
                        )

                    case '<':
                        self.button = SymbolDeletionButton(
                            master=self,
                            text=button_text,
                            output_field=self.output_field
                        )

                    case '=':
                        self.button = CalculationButton(
                            master=self,
                            text=button_text,
                            output_field=self.output_field
                        )
                    
                    case _:
                        self.button = Button(
                            master=self,
                            text=button_text,
                            output_field=self.output_field
                        )

                self.button.grid(row=i+1, column=j, pady=5, padx=5)


if __name__ == '__main__':
    calculator = Calculator()
    calculator.mainloop()