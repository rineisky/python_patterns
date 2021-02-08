class GameConsole:
    def create_game_picture(self):
        return f'picture from console'


class Antenna:
    def create_antenna_picture(self):
        return f'picture from antenna'


class SourceGameConsole(GameConsole):
    def get_picture(self):
        return self.create_game_picture()


class SourceAntenna(Antenna):
    def get_picture(self):
        return self.create_antenna_picture()


class TV:
    def __init__(self, source):
        self.source = source

    def show_picture(self):
        return self.source.get_picture()


if __name__ == '__main__':
    g = SourceGameConsole()
    a = SourceAntenna()
    game_picture = TV(g)
    antenna_picture = TV(a)
    print(game_picture.show_picture())
    print(antenna_picture.show_picture())
