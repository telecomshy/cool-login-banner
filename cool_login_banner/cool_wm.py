from colorama import Fore
from fabric import Connection
from invoke import sudo
from functools import partial
from pathlib import Path
from tempfile import TemporaryFile


class CoolLoginBanner:
    SSHD_CONFIG_PATH = '/etc/ssh/sshd_config'
    SSH_BANNER_PATH = '/etc/ssh/ssh_login_banner'
    MOTD_PATH = '/etc/motd'
    ISSUE_PATH = '/etc/issue'
    ISSUE_NET_PATH = '/etc/issue_net'

    def __init__(self, host=None, *, encoding='utf8', sudo_pass=None, **kwargs):
        self.banner = None
        if host:
            self.conn = Connection(host, **kwargs)
            sudo_pass = sudo_pass or self.conn.connect_kwargs.get('password', None)
            self.sudo = partial(self.conn.sudo, encoding=encoding, password=sudo_pass)
        else:
            self.sudo = partial(sudo, encoding=encoding, password=sudo_pass)

    def generate_banner(self, engine, *, preview=True, **kwargs):
        self.banner = engine(**kwargs)
        if preview:
            print(self.banner)
        return self.banner

    def _upload_file(self, banner_str, remote_abs_path):
        self.conn.put('tmp_banner_file', '/tmp')
        self.sudo(f'mv /tmp/tmp_banner_file {remote_abs_path}')
        self.sudo(f'rm -f /tmp/tmp_banner_file')
        Path('tmp_banner_file').unlink()

    def set_ssh_banner(self, banner_str):
        self.sudo(f"bash -c 'echo \"Banner /etc/ssh/ssh_login_banner\" >> {self.SSHD_CONFIG_PATH}'")
        self._upload_file(banner_str, '/etc/ssh/ssh_login_banner')
        self.sudo('systemctl restart sshd')

    def reset_ssh_banner(self):
        self.sudo('rm -f /etc/ssh/ssh_login_banner')
        self.sudo('sed -i /^Banner/d /etc/ssh/sshd_config')
        self.sudo('systemctl restart sshd')

    def set_banner_after_login(self, banner_str):
        pass

    def reset_banner_after_login(self):
        pass

    def set_tty_banner(self, banner_str):
        pass

    def reset_tty_banner(self):
        pass

    def set_telnet_banner(self, banner_str):
        pass

    def reset_telnet_banner(self):
        pass

