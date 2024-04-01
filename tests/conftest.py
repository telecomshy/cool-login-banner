import pytest
from cool_login_banner import TextEngine, FigletEngine, CowsayEngine, BannerSetter
from unittest.mock import patch, MagicMock


@pytest.fixture
def text_engine(scope="module"):
    return TextEngine()


@pytest.fixture
def figlet_engine(scope="module"):
    return FigletEngine()


@pytest.fixture
def cowsay_engine(scope="module"):
    return CowsayEngine()


@pytest.fixture()
def banner_setter():
    mock_engine = MagicMock()
    setter = BannerSetter(mock_engine)
    setter.conn = MagicMock(name='conn')
    setter.sudo = MagicMock(name='sudo')
    return setter

