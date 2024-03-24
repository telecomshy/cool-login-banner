Cool Login Banner
==================

说明
---------
这个小玩意，可以快捷方便的定制你的linux登录界面，比如:

.. code-block::
    from cool_login_banner import CoolLoginBanner, CowsayEngine

    clb = CoolLoginBanner(CowsayEngine, host='192.168.0.33', user='username', password='passoword')
    clb.set_ssh_banner(text="A python enthusiast's site", animal_name='cow', fore_color='lightyellow_ex', styles=['blink'])


然后再次登录，你的登录界面就变成这样了：

.. image:: docs/img/login_banner.gif

