from cool_login_banner import FigletEngine, BannerSetter
from unittest.mock import call, sentinel, patch


def test_init_banner_setter():
    setter = BannerSetter()
    assert setter.engine is None
    setter = BannerSetter(FigletEngine)
    assert isinstance(setter.engine, FigletEngine)


def test_init_banner_setter_host_arg(capsys):
    setter = BannerSetter()
    assert setter.conn is None
    assert setter.sudo is sentinel.partial_sudo


def test_save_text_to_file():
    setter = BannerSetter(host="host")
    setter._save_text_to_file("faketext", "fakefile")
    calls = [call("mv -f /tmp/tmp_banner fakefile"), call("chown root:root fakefile")]
    assert setter.sudo.call_args_list == calls

