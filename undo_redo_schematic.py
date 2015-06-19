from automa import api as automa
from automa.api import *

class Undo_Redo_Schematic:
    @staticmethod
    def run():
        if Image(r'Images\button_undo_disabled.png').exists() and Image(r'Images\button_redo_disabled.png'):
            click(Image(r'Images\category.png'))
            click(Image(r'Images\sub_category.png'))
            wait_until(Image(r'Images\target_part.png').exists)
            click(Image(r'Images\target_part.png'))
            click(Image(r'Images\schematic_blank.png'))
            press(ESC)
            click(Image(r'Images\button_undo_enabled.png'))