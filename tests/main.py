from cool_login_banner import BannerSetter, CowsayEngine, TextEngine

text_engine = TextEngine()
cowsay_engine = CowsayEngine()
banner_setter = BannerSetter(host='192.168.17.10', user='username', password='password')

# note_msg1 = "1. You must be a pretty girl\n"
# note_msg2 = "2. You must be over 18 years old\n"
#
# note_banner1 = text_engine.generate_banner(note_msg1, fore_color='red', styles=['blink'])
# note_banner2 = text_engine.generate_banner(note_msg2, back_color='blue', styles=['blink'])
# cowsay_banner = cowsay_engine.generate_banner('welcome, lovely girl', pattern='tux')
#
# banner = note_banner1 + note_banner2 + cowsay_banner
# banner_setter.save_ssh_banner(banner)


print(cowsay_engine.fore_colors)