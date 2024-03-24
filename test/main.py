from cool_login_banner import CoolLoginBanner, CowsayEngine, FigletEngine, TextEngine
from pyfiglet import figlet_format, Figlet
from colorama import init, Back, Fore, just_fix_windows_console
from termcolor import colored

cl = CoolLoginBanner(TextEngine, host='192.168.44.131', user='shy', password='shy501024')
# cl.preview_styles()

cl.set_ssh_banner(text='fuck off', fore_color='red', back_color='blue', styles=['blink', 'underline'])

