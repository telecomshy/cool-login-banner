class TestTextEngine:
    def test_fore_colors(self, text_engine):
        assert 'black'.upper() in text_engine.fore_colors

    def test_back_colors(self, text_engine):
        assert 'red'.upper() in text_engine.back_colors

    def test_styles(self, text_engine):
        assert 'underline' in text_engine.styles

    def test_preview_fore_colors(self, text_engine, capsys):
        text_engine.preview_fore_colors()
        out, err = capsys.readouterr()
        assert 'black'.upper() in out

    def test_preview_back_colors(self, text_engine, capsys):
        text_engine.preview_back_colors()
        out, err = capsys.readouterr()
        assert 'black'.upper() in out

    def test_preview_styles(self, text_engine, capsys):
        text_engine.preview_styles()
        out, err = capsys.readouterr()
        assert 'bold' in out


class TestFigletEngine:
    def test_generate_origin_banner(self, figlet_engine, capsys):
        banner = figlet_engine.generate_original_banner("hello world")
        assert banner

    def test_generate_banner(self, figlet_engine):
        banner = figlet_engine.generate_banner(text='hello', styles=['blink'])
        assert '\x1b[5m' in banner

    def test_figet_fonts(self, figlet_engine):
        assert 'doom' in figlet_engine.figlet_fonts


class TestCowsayEngine:
    def test_generate_origin_banner(self, cowsay_engine):
        banner = cowsay_engine.generate_original_banner('hello world')
        assert 'hello world' in banner

    def test_generate_banner(self, cowsay_engine):
        banner = cowsay_engine.generate_banner('hello world', styles=['bold'])
        assert 'hello world' in banner
        assert '\x1b[1m' in banner

    def test_patterns(self, cowsay_engine):
        assert 'tux' in cowsay_engine.patterns

    def test_preview_patterns(self, cowsay_engine, capsys):
        cowsay_engine.preview_patterns()
        out, err = capsys.readouterr()
        assert 'cow' in out
