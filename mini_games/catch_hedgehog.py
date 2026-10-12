import webbrowser

from mini_game import MiniGame


class CatchHedgehogMiniGame(MiniGame):
    def __init__(self):
        super().__init__()
        self.name = "Złap jeża!"
        url = "https://www.grajteraz.pl/przygoda/ultimate-flash-sonic"
        webbrowser.open(url)