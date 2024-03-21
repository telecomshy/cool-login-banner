from pyfiglet import figlet_format as figlet_engine
from cowsay import get_output_string as cowsay_engine
from colorama import Fore
from .executors import SshCmdExecutor, LocalCmdExecutor


class CoolWM:
    def __init__(self, host=None, *, encoding='utf8', sudo_pass=None, **kwargs):
        self.wm = None
        if host:
            self.excutor = SshCmdExecutor(host, encoding=encoding, sudo_pass=sudo_pass, **kwargs)
        else:
            self.excutor = LocalCmdExecutor(encoding=encoding, sudo_pass=sudo_pass)

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


