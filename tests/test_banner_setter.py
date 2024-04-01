from cool_login_banner import FigletEngine, BannerSetter
from unittest.mock import call, sentinel, patch, ANY


def test_init_banner_setter():
    setter = BannerSetter()
    assert setter.engine is None
    setter = BannerSetter(FigletEngine)
    assert isinstance(setter.engine, FigletEngine)


def test_init_banner_setter_with_host():
    setter = BannerSetter()
    assert setter.conn is None

    setter = BannerSetter(host="fake_host")
    setter.conn.host = "fake_host"




