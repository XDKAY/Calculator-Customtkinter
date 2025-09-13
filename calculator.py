import customtkinter


TITLE = 'Calculator'
WINDOW_SIZE = (445, 750)
IS_ANSWER = False
TEXT_BUTTONS = (
    ('C', '(', ')', '+'),
    ('1', '2', '3', '-'),
    ('4', '5', '6', 'x'),
    ('7', '8', '9', '/'),
    ('0', '.', '%', '<'),
    ('=', '^', '^2', '')
)


def calculate(output_field:customtkinter.CTkTextbox):
    data = output_field.get('0.0', 'end').replace('^', '**').replace('x', '*')
    clean_output_area(output_field)

    try:
        global IS_ANSWER
        result = f'{eval(data)}'
        output_field.insert('0.0', result)
        IS_ANSWER = True
        

    except ZeroDivisionError:
        output_field.insert('0.0', 'division by zero')
    
    except SyntaxError:
        output_field.insert('0.0', 'invalid syntax')


def clean_output_area(output_field:customtkinter.CTkTextbox):
    output_field.delete('0.0', 'end')


def remove_last_symbol(output_field:customtkinter.CTkTextbox):
    data = output_field.get('0.0', 'end')[:-1]
    clean_output_area(output_field)

    if IS_ANSWER:
        output_field.insert('0.0', '')
    else:
        output_field.insert('0.0', data[:-1])


def click(value:str, output_field:customtkinter.CTkTextbox):
    global IS_ANSWER

    data = output_field.get('0.0', 'end')

    if data.startswith('division by zero') or data.startswith('invalid syntax') or IS_ANSWER and value.isdigit():
        clean_output_area(output_field)

    output_field.insert('end', value)
    IS_ANSWER = False


def main():
    app = customtkinter.CTk()
    app.grid_columnconfigure((0, 1, 2, 3), weight=1)

    app.title(TITLE)
    app.geometry(f'{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}')

    output_field = customtkinter.CTkTextbox(
            app,
            width=app.winfo_screenwidth(),
            height=int(WINDOW_SIZE[1]*0.11),
            font=('Arial', 40),
            corner_radius=10,
            fg_color='#33383f',
            wrap='none',
            activate_scrollbars=True,
            xscrollcommand=True,
            yscrollcommand=False
        )

    output_field.grid(row=0, column=0, columnspan=4, pady=5, padx=5)

    for i in range(len(TEXT_BUTTONS)):
        for j in range(len(TEXT_BUTTONS[i])):

            text_button = TEXT_BUTTONS[i][j]

            match text_button:
                case 'C':
                    button = customtkinter.CTkButton(
                        app,
                        width=app.winfo_screenwidth(),
                        height=100,
                        text=text_button,
                        font=('Arial', 50),
                        fg_color ='#ab7dfb',
                        hover_color='#7b5bb7',
                        corner_radius=10,
                        command=lambda output_field=output_field: clean_output_area(output_field)
                    )

                case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '0':
                    button = customtkinter.CTkButton(
                        app,
                        width=app.winfo_screenwidth(),
                        height=100,
                        text=text_button,
                        font=('Arial', 50),
                        fg_color='#ff9900',
                        hover_color='#b56900',
                        corner_radius=10,
                        command=lambda text_button=text_button, output_field=output_field: click(text_button, output_field),
                    )

                case '<':
                    button = customtkinter.CTkButton(
                        app,
                        width=app.winfo_screenwidth(),
                        height=100,
                        text=text_button,
                        font=('Arial', 50),
                        fg_color ='#ab7dfb',
                        hover_color='#7b5bb7',
                        corner_radius=10,
                        command=lambda output_field=output_field: remove_last_symbol(output_field)
                    )

                case '=':
                    button = customtkinter.CTkButton(
                        app,
                        width=app.winfo_screenwidth(),
                        height=100,
                        text=text_button,
                        font=('Arial', 50),
                        fg_color='#50ce6d',
                        hover_color='#3da052',
                        corner_radius=10,
                        command=lambda output_field=output_field: calculate(output_field)
                    )
                
                case _:
                    button = customtkinter.CTkButton(
                        app,
                        width=app.winfo_screenwidth(),
                        height=100,
                        text=text_button,
                        font=('Arial', 50),
                        fg_color='#ab7dfb',
                        hover_color='#7b5bb7',
                        corner_radius=10,
                        command=lambda text_button=text_button, output_field=output_field: click(text_button, output_field),
                    )

            button.grid(row=i+1, column=j, pady=5, padx=5)

    app.mainloop()


if __name__ == '__main__':
    main()