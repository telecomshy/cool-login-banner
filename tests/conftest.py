import pytest
from cool_login_banner import TextEngine, FigletEngine, CowsayEngine


@pytest.fixture
def text_engine(scope="module"):
    return TextEngine()


@pytest.fixture
def figlet_engine(scope="module"):
    return FigletEngine()


@pytest.fixture
def cowsay_engine(scope="module"):
    return CowsayEngine()