class Config:
    TITLE = 'Calculator'

    WINDOW_SIZE = (445, 750)

    CORNER_RADIUS = 10

    FONT = ('Arial', 50)

    # Textbox
    FG_COLOR_TEXTBOX = '#33383f'

    # Button
    DEFAULT_BUTTON_HEIGHT = 100

    BUTTONS_TEXT = (
        ('C', '(', ')', '+'),
        ('1', '2', '3', '-'),
        ('4', '5', '6', 'x'),
        ('7', '8', '9', '/'),
        ('0', '.', '%', '<'),
        ('=', '^', '^2', '')
    )
    
    FG_COLOR_BUTTON = '#ab7dfb'
    HOVER_COLOR_BUTTON = '#7b5bb7'
    DIGIT_FG_COLOR_BUTTON = '#ff9900'
    DIGIT_HOVER_COLOR_BUTTON = '#b56900'
    FG_COLOR_CALCULATION_BUTTON = '#50ce6d'
    HOVER_COLOR_CALCULATION_BUTTON = '#3da052'