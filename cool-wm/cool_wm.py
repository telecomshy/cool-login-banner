from pyfiglet import figlet_format as figlet_engine
from cowsay import get_output_string as cowsay_engine
from colorama import Fore
from fabric import Connection
from invoke import sudo
from functools import partial


class CoolWM:
    def __init__(self, host=None, *, encoding='utf8', sudo_pass=None, **kwargs):
        self.wm = None
        sudo_pass = sudo_pass or kwargs.get('connect_kwargs').get('password')
        excutor = Connection(host, **kwargs).sudo if host else sudo
        self.excute = partial(excutor, encoding=encoding, password=sudo_pass)

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


if __name__ == '__main__':
    cl = CoolWM(host='192.168.44.131', user='telecomshy', connect_kwargs={'password': 'shy501024'})
    # cl.excute('pwd')
    cl.generate_wm(figlet_engine, text='hello world', font='boom')
    # pyfiglet.FigletFont.getFonts()

