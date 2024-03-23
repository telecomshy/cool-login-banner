from fabric import Connection
from invoke import sudo
from functools import partial
from pathlib import Path


class CoolLoginBanner:
    SSHD_CONFIG_PATH = '/etc/ssh/sshd_config'
    SSH_BANNER_PATH = '/etc/ssh/login_banner'
    MOTD_PATH = '/etc/motd'
    ISSUE_PATH = '/etc/issue'
    ISSUE_NET_PATH = '/etc/issue_net'

    def __init__(self, engine, *, host=None, port=22, user=None, password=None, encoding='utf8', **kwargs):
        self.engine = engine()
        if host:
            connect_kwargs = kwargs.setdefault('connect_kwargs', {})
            connect_kwargs['password'] = password
            self.conn = Connection(host, user=user, port=port, **kwargs)
            self.sudo = partial(self.conn.sudo, encoding=encoding, password=password, hide=True)
        else:
            self.sudo = partial(sudo, encoding=encoding, password=password, hide=True)

    def generate_banner(self, preview=True, **kwargs):
        banner = self.engine.generate_banner(**kwargs)
        if preview:
            print(banner)
        return banner

    def _save_banner_to_file(self, banner, file):
        with open('tmp_banner', 'wt') as f:
            f.write(banner)
        self.conn.put('tmp_banner', '/tmp')
        self.sudo(f'mv /tmp/tmp_banner {file}')
        self.sudo(f'rm -f /tmp/tmp_banner')
        Path('tmp_banner').unlink(missing_ok=True)

    def _clear_file(self, file):
        self.sudo(f'sed -i "/^/d" {file}')

    def set_ssh_banner(self, banner):
        self.sudo(f"sed -i -r '/^#?Banner/a Banner {self.SSH_BANNER_PATH}' {self.SSHD_CONFIG_PATH}")
        self._save_banner_to_file(banner, self.SSH_BANNER_PATH)
        self.sudo('systemctl restart sshd')

    def clear_ssh_banner(self):
        self.sudo(f'rm -f {self.SSH_BANNER_PATH}')
        self.sudo(f'sed -i /^Banner/d {self.SSHD_CONFIG_PATH}')
        self.sudo('systemctl restart sshd')

    def set_banner_after_login(self, banner):
        self._save_banner_to_file(banner, self.MOTD_PATH)

    def clear_banner_after_login(self):
        self._clear_file(self.MOTD_PATH)

    def set_tty_banner(self, banner):
        self._save_banner_to_file(banner, self.ISSUE_PATH)

    def clear_tty_banner(self):
        self._clear_file(self.ISSUE_PATH)

    def set_telnet_banner(self, banner):
        self._save_banner_to_file(banner, self.ISSUE_NET_PATH)

    def clear_telnet_banner(self):
        self._clear_file(self.ISSUE_NET_PATH)
