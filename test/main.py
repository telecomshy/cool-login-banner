from cool_login_banner import BannerSetter, CowsayEngine, FigletEngine, TextEngine
from pyfiglet import figlet_format, Figlet
from colorama import init, Back, Fore, just_fix_windows_console
from termcolor import colored

clb = BannerSetter(CowsayEngine, host='192.168.17.10', user='root', password='shy501024')
# cl.preview_fore_colors()

text = """
1. this site is a test site
2. if you don't have account, please contact telecomshy
"""
clb.set_ssh_banner(text='hello', name='fox')
# clb.clear_ssh_banner()
