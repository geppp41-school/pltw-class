
class Map:
    def __init__(self) -> None:
        self.__nodes__ = []
        pass
    def get_node (self, x: int, y: int):
        return self.__nodes__[y][x]
    pass