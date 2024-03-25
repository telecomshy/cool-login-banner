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
    - `修改不同的banner`_
    - `引擎通用方法`_

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

    bs.clear_ssh_banner()

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

如果是远程登陆，所有关键字参数都会送给 ``fabric.Connection``, 除了 ``password`` 参数。因为 ``Connection``
如果需要设置登陆密码，需要在 ``connect_kwargs`` 这个关键字参数里面设置，我觉得很不方便，进行了合并。

本机执行程序的话，除了 ``engine``, 就不用传递额外参数了。不过不管是远程还是本机，账号需要有sudo的权限，如果sudo
需要密码，则需要提供 ``password`` 参数。

修改不同的banner
~~~~~~~~~~~~~~~~~~~

``BannerSetter`` 对象提供了四个方法，分别修改不同的login登陆页面：

- ``set_ssh_banner`` : 设置ssh远程登陆的banner，此登陆之前显示。内部修改 /etc/ssh/sshd_config 文件
- ``set_motd_banner`` : 设置成功登陆以后的banner。内部修改 /etc/motd 文件。
- ``set_tty_banner`` : 设置本机终端登陆的banner，在登陆之前显示。内部修改 /etc/issue 文件。
- ``set_telnet_banner`` : 设置telnet远程登陆的banner，在登陆之前显示。内部修改 /etc/issue_net 文件。

引擎通用方法
~~~~~~~~~~~~~~~~

所有引擎都可以通过 ``fore_color``, ``back_color``, ``styles`` 关键字参数设置前景色，背景色以及风格。
并且提供了以下几个方法查看内置的颜色或者进行预览：

.. code-block::

    engine.fore_colors                  # 查看所有前景色名称
    engine.back_colors                  # 查看所有背景色名称
    engine.styles                       # 查看所有风格
    engine.preview_fore_colors()        # 预览前景色
    engine.preview_back_colors()        # 预览背景色
    engine.preview_styles()             # 预览风格

.. note::

    可以在 ``BannerSetter`` 实例上调用所有 ``engine`` 的方法

figlet引擎
~~~~~~~~~~~~~~~~

cowsay引擎
~~~~~~~~~~~~~~~~

自定义banner
~~~~~~~~~~~~~~~~

