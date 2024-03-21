from cool_wm.cool_wm import CoolWM

cl = CoolWM(host='192.168.44.131', user='telecomshy', connect_kwargs={'password': 'shy501024'})
cl.excutor.sudo('pwd')