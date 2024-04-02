from cool_login_banner import FigletEngine, BannerSetter
from unittest.mock import call, patch, ANY


def test_init_banner_setter():
    setter = BannerSetter()
    assert setter.engine is None
    setter = BannerSetter(FigletEngine)
    assert isinstance(setter.engine, FigletEngine)


def test_init_banner_setter_with_host():
    setter = BannerSetter()
    assert setter.conn is None

    setter = BannerSetter(host="fake_host")
    assert setter.conn.host == "fake_host"


def test_save_text_to_file(banner_setter):
    banner_setter._save_text_to_file("content", "fakefile")
    banner_setter.conn.put.assert_called_once_with(ANY, "/tmp/tmp_banner")
    calls = [call("mv -f /tmp/tmp_banner fakefile"), call("chown root:root fakefile")]
    assert banner_setter.sudo.call_args_list == calls
