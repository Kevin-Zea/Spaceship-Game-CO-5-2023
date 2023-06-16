from game.utils.constants import FONT_STYLE
from pygame.font import Font

def get_message(message, size, color, width, heigth):
    font = Font(FONT_STYLE, size)
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (width, heigth)
    return text, text_rect