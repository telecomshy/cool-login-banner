import cowsay
import pyfiglet
from abc import ABC, abstractmethod
from colorama import Fore, Back, init


class Engine(ABC):
    def __init__(self):
        init(autoreset=True)

    @abstractmethod
    def generate_original_banner(self, **kwargs):
        pass

    def generate_banner(self, *, fore_color=None, back_color=None, **kwargs):
        banner = self.generate_original_banner(**kwargs)
        if fore_color is not None:
            banner = getattr(Fore, fore_color.upper()) + banner
        if back_color is not None:
            banner = getattr(Back, back_color.upper()) + banner
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


class FigletEngine(Engine):
    def generate_original_banner(self, **kwargs):
        return pyfiglet.figlet_format(**kwargs)

    @property
    def fonts(self):
        return pyfiglet.FigletFont.getFonts()


class CowsayEngine(Engine):
    def generate_original_banner(self, **kwargs):
        return cowsay.get_output_string(**kwargs) + '\n'

    @property
    def char_names(self):
        return cowsay.char_names

    @staticmethod
    def preview_char(char):
        getattr(cowsay, char)('hello world')
