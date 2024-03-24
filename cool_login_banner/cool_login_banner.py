from fabric import Connection
from invoke import sudo
from functools import partial
from io import BytesIO


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

    def _save_text_to_file(self, text, file):
        with BytesIO(text.encode('utf8')) as f:
            self.conn.put(f, '/tmp/tmp_banner')
            self.sudo(f'mv -f /tmp/tmp_banner {file}')
            self.sudo(f'chown root:root {file}')

    def _clear_file_content(self, file):
        self.sudo(f'sed -i "/^/d" {file}')

    def save_ssh_banner(self, banner):
        self.sudo(f"sed -i -r '/^#?Banner/a Banner {self.SSH_BANNER_PATH}' {self.SSHD_CONFIG_PATH}")
        self._save_text_to_file(banner, self.SSH_BANNER_PATH)
        self.sudo('systemctl restart sshd')

    def set_ssh_banner(self, *args, **kwargs):
        banner = self.generate_banner(*args, **kwargs)
        self.save_ssh_banner(banner)

    def clear_ssh_banner(self):
        self.sudo(f'rm -f {self.SSH_BANNER_PATH}')
        self.sudo(f'sed -i /^Banner/d {self.SSHD_CONFIG_PATH}')
        self.sudo('systemctl restart sshd')

    def save_motd_banner(self, banner):
        self._save_text_to_file(banner, self.MOTD_PATH)

    def clear_motd_banner(self):
        self._clear_file_content(self.MOTD_PATH)

    def set_motd_banner(self, *args, **kwargs):
        banner = self.generate_banner(*args, **kwargs)
        self.save_motd_banner(banner)

    def save_tty_banner(self, banner):
        self._save_text_to_file(banner, self.ISSUE_PATH)

    def clear_tty_banner(self):
        self._clear_file_content(self.ISSUE_PATH)

    def set_tty_banner(self, *args, **kwargs):
        banner = self.generate_banner(*args, **kwargs)
        self.save_tty_banner(banner)

    def save_telnet_banner(self, banner):
        self._save_text_to_file(banner, self.ISSUE_NET_PATH)

    def clear_telnet_banner(self):
        self._clear_file_content(self.ISSUE_NET_PATH)

    def set_telnet_banner(self, *args, **kwargs):
        banner = self.generate_banner(*args, **kwargs)
        self.save_telnet_banner(banner)

    def __getattr__(self, name):
        return getattr(self.engine, name)
