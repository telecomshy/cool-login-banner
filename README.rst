Cool Login Banner
==================

方便快捷的定制你的linux登录界面:

.. image:: ./docs/img/login_banner.gif
    :width: 400

目录
===========

- `安装`_
- `描述`_
- `基本用法`_
    - `远程或本地`_

安装
----------

尚未发布...

描述
----------

Cool Login Banner 设置主机登陆界面最快只需要2步：

1. 创建 ``BannerSetter`` 对象。
2. 调用不同的方法设置对应的登陆banner。

.. code-block:: python

    from cool_login_banner import BannerSetter, CowsayEngine

    bs = BannerSetter(CowsayEngine, host='192.168.44.131', user='username', port=22, password='password')
    bs.set_ssh_banner(text="A python enthusiast's site", name='cow', fore_color='lightyellow_ex', styles=['blink'])

恢复也很容易：

.. code-block:: python

    clb.clear_ssh_banner()

除了远程，也可以设置本机的登陆banner。

基于 ``colorama``, ``pyfiglet`` 和 ``cowsay``, 一共有三种不同风格的banner引擎：

.. image:: ./docs/img/text_engine.png
    :width: 400

.. image:: ./docs/img/figlet_engine.png
    :width: 400

.. image:: ./docs/img/cowsay_engine.png
    :width: 400

基本用法
--------

远程或本地
~~~~~~~~~~~~~

``BannerSetter`` 类会根据是否传递 ``host`` 参数来判断是远程连接还是本地执行。



修改不同的banner
~~~~~~~~~~~~~~~~~~~

``BannerSetter`` 对象提供了四个方法，分别修改不同的login登陆页面：

- ``set_ssh_banner`` : 设置ssh远程登陆的banner，此登陆之前显示。内部修改 /etc/ssh/sshd_config 文件
- ``set_motd_banner`` : 设置成功登陆以后的banner。内部修改 /etc/motd 文件。
- ``set_tty_banner`` : 设置本机终端登陆的banner，在登陆之前显示。内部修改的是 /etc/issue 文件。
- ``set_telnet_banner`` : 设置telnet远程登陆的banner，在登陆之前显示。内部修改的是 /etc/issue_net 文件。

通用引擎方法
~~~~~~~~~~~~~~~~


figlet引擎
~~~~~~~~~~~~~~~~

cowsay引擎
~~~~~~~~~~~~~~~~



