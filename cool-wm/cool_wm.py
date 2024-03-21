from pyfiglet import figlet_format as figlet_engine
from cowsay import get_output_string as cowsay_engine
from colorama import Fore


class CoolWM:
    def __init__(self):
        self.wm = None

    def generate_wm(self, engine, *, preview=True, color=None, **kwargs):
        self.wm = engine(**kwargs)
        if color:
            self.wm = getattr(Fore, color.upper()) + self.wm
        if preview:
            print(self.wm)
        return self.wm

    def save(self, path='/etc/motd'):
        if self.wm is None:
            raise ValueError("Please generate logo at first!")

        with open(path, 'wt') as f:
            f.write(self.wm)

    def change(self, text, *, color=None, char=None, font='doom'):
        if char:
            self.generate_wm(cowsay_engine, text=text, color=color, char=char)
        else:
            self.generate_wm(figlet_engine, text=text, color=color, font=font)


if __name__ == '__main__':
    cl = CoolWM()
    cl.change('hello world', color='green')
