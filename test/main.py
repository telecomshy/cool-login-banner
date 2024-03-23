from cool_login_banner.cool_wm import CoolLoginBanner
from pyfiglet import figlet_format

cl = CoolLoginBanner(host='192.168.44.131', user='telecomshy', connect_kwargs={'password': 'shy501024'})
wm = cl.generate_banner(figlet_format, text='telecomshy host')
# cl.set_ssh_banner(wm)
cl.reset_ssh_banner()