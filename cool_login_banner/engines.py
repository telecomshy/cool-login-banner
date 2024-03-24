import cowsay
import pyfiglet
import termcolor
from abc import ABC, abstractmethod
from colorama import Fore, Back, Style, just_fix_windows_console
from termcolor import colored

just_fix_windows_console()

STYLE_LST = {
    'blink': '\x1b[5m',
    'bold': '\x1b[1m',
    'underline': '\x1b[4m',
    'reverse': '\x1b[7m',
    'strikethrough': '\x1b[9m',
}


class Engine(ABC):

    @abstractmethod
    def generate_original_banner(self, *args, **kwargs):
        pass

    def generate_banner(self, *, fore_color=None, back_color=None, styles=None, preview=True, **kwargs):
        banner = self.generate_original_banner(**kwargs)
        if fore_color is not None:
            banner = getattr(Fore, fore_color.upper()) + banner
        if back_color is not None:
            banner = getattr(Back, back_color.upper()) + banner
        if styles is not None:
            banner = ''.join([STYLE_LST[s] for s in styles if s in STYLE_LST] + [banner])
        banner = banner + Style.RESET_ALL
        if preview:
            print(banner)
        return banner

    @property
    def fore_colors(self):
        return list(Fore.__dict__.keys())

    @property
    def back_colors(self):
        return list(Back.__dict__.keys())

    @staticmethod
    def preview_fore_colors():
        for color in Fore.__dict__:
            print(getattr(Fore, color.upper()) + color)

    @staticmethod
    def preview_back_colors():
        for color in Back.__dict__:
            print(getattr(Back, color.upper()) + color)

    @staticmethod
    def preview_styles():
        for name, code in STYLE_LST.items():
            print(f'{code}{name}{termcolor.RESET}')


class TextEngine(Engine):
    def generate_original_banner(self, text):
        return text


class FigletEngine(Engine):
    def generate_original_banner(self, text, font, **kwargs):
        return pyfiglet.figlet_format(text, font, **kwargs)

    @property
    def figlet_fonts(self):
        return pyfiglet.FigletFont.getFonts()


class CowsayEngine(Engine):
    def generate_original_banner(self, animal_name, text):
        if animal_name in self.animal_names:
            return cowsay.get_output_string(animal_name, text) + '\n'
        else:
            return cowsay.draw(text, animal_name, False)

    @property
    def animal_names(self):
        return cowsay.char_names

    @staticmethod
    def preview_animal(animal):
        getattr(cowsay, animal)(animal)
