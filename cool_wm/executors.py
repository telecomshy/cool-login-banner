from fabric import Connection
from invoke import sudo
from functools import partial


class Executor:
    def save_to_motd(self):
        pass


class SshCmdExecutor(Executor):
    def __init__(self, host, *, encoding='utf8', sudo_pass=None, **kwargs):
        kwargs['host'] = host
        self.conn = Connection(**kwargs)
        sudo_pass = sudo_pass or self.conn.connect_kwargs.get('password', None)
        self.sudo = partial(self.conn.sudo, encoding=encoding, password=sudo_pass)

    def save_to_issue(self):
        pass


class LocalCmdExecutor(Executor):
    def __init__(self, encoding='utf8', sudo_pass=None):
        self.sudo = partial(sudo, encoding=encoding, password=sudo_pass)

    def save_to_issue(self):
        pass
