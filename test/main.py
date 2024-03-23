from cool_login_banner import CoolLoginBanner, CowsayEngine, FigletEngine
from pyfiglet import figlet_format, Figlet
from colorama import init, Back, Fore

cl = CoolLoginBanner(CowsayEngine, host='192.168.44.131', user='shy', password='shy501024')
banner = cl.generate_banner(text='fuck off', char='fox')
# cl.set_banner_after_login(banner)

cl.clear_banner_after_login()
# cl.clear_ssh_banner()
