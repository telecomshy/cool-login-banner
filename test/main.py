from cool_login_banner import BannerSetter, CowsayEngine, FigletEngine, TextEngine
from pyfiglet import figlet_format, Figlet
from colorama import init, Back, Fore, just_fix_windows_console
from termcolor import colored

clb = BannerSetter(CowsayEngine, host='133.0.182.136', port=53922, user='root2', password='wzdx!@#$')
# cl.preview_fore_colors()

clb.set_ssh_banner(text="YSX web server, no entry without permission", name='cow', fore_color='lightyellow_ex')

