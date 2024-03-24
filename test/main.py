from cool_login_banner import BannerSetter, CowsayEngine, FigletEngine, TextEngine
from pyfiglet import figlet_format, Figlet
from colorama import init, Back, Fore, just_fix_windows_console
from termcolor import colored

clb = BannerSetter(CowsayEngine, host='192.168.44.131', user='shy', password='shy501024')
# cl.preview_fore_colors()

clb.set_ssh_banner(text="A python enthusiast's site", animal_name='cow', fore_color='lightyellow_ex', styles=['blink'])

