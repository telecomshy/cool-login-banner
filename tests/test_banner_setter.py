from cool_login_banner import BannerSetter, TextEngine
from unittest.mock import patch


def test_init_banner_setter():
    banner = BannerSetter()
    assert banner.engine is None
    banner = BannerSetter(TextEngine)
    isinstance(banner.engine, TextEngine)

    # 测试BannerSetter是否可以正常接收Engine参数
    with patch('cool_login_banner.banner_setter.Connection') as mock_connection:
        with patch('cool_login_banner.banner_setter.partial') as mock_partial:
            banner = BannerSetter(host='fakehost')
            mock_connection.assert_called_once()
            mock_partial.assert_called_once()


def test_save_text_to_file(banner_setter):
    banner_setter._save_text_to_file('content', 'file')
    banner_setter.conn.put.assert_called_once()
    banner_setter.sudo.assert_any_call('mv -f /tmp/tmp_banner file')
    banner_setter.sudo.assert_any_call('chown root:root file')
