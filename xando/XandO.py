# Игра в крестики нолики
import pygame as pg
from enum import Enum


CELL_SIZE = 50
FPS = 60

class Cell(Enum):
    """
    
    """
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Класс игрока, содержащий тип значков и имя.
    """
    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type
        

class GameField:
    """
    
    """
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID]*self.width for i in range(self.height)]


class GameFieldView:
    """
    Виджет игрового поля, который отображает его на экране, а также выясняет место клика.
    """
    def __init__(sefl, field):
        # загрузить картинки значков клеток.
        # отобразить первичное поле.
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        return True # TODO: self._height учесть

    def get_coords(self, x, y):
        return 0, 0 # TODO: реально вычислить клетку клика
    

class GameRoundManager:
    """
    Менеджер игры, запускающий все процессы.
    """
    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.field = GameField()

    def handle_click(self):
        player = self._players[self._current_player]
        #грок делает клик на игровом поле
        print("click_handled", i, j)
            
   
class GameWindow:
    """
    Содержит виджет поля,
    а также менеджера игрового раунда.
    """
    def __init__(self):
        # инициализация pygame
        pg.init()

        # Window
        self._width = 800
        self._height = 600
        self._title = "Crosses & Zeroes"
        self._screen = pg.display.set_mode(self._width, self._height)
        pg.display.set_caption(self._title)


        self._field_widget = GameFieldView()
        player1 = Player("Петя", Cell.CROSS)
        player2 = Player("Вася", Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        
        
    def main_loop(self):
        finished = False
        clock = pg.time.Clock()
        while not finished:
            for event in pg.events.get(...):
                if event.type == pg.QUIT:
                    finished = True
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    x, y = mouse_pos
                    
                    if self._field_widget.check_coords_correct(x, y):              
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)
            pg.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print("Game Over!")


if __name__ == "__main__":
    main()

