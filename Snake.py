import config
from direction import Direction

if config.DEBUG_MODE_ON:
    import Debug

class Snake(list):
    
    def __init__(self):
        self._HEAD_IDX = 0
        self._curr_dir = None
        if config.DEBUG_MODE_ON:
            self._snake = Debug.DEBUG_SNAKE
        else:
            self._snake = [config.DEFAULT_HEAD_COORD]

        self._pending_Growth = False

    def snake_coords(self) -> list[list[int]]:
        return self._snake
    
    def __len__(self) -> int:
        return len(self._snake)

    def __str__(self):
        returnStr = ""
        for elem in self._snake:
            returnStr += str(elem)
        return returnStr

    def current_direction(self):
        return self._curr_dir

    def _toggleGrow(self):
        if self._pending_Growth:
            self._pending_Growth = False
        else:
            self._pending_Growth = True

    def move(self, dir:Direction):
        
        if dir == Direction.UP:
            self._move_up()
        if dir == Direction.DOWN:
            self._move_down()
        if dir == Direction.LEFT:
            self._move_left()
        if dir == Direction.RIGHT:
            self._move_right()
            
    def _move_up(self):
        self._snake.insert(0, (self._snake[0][0], self._snake[0][1] - 1))
        if self._pending_Growth == False:
            self._snake.pop()
        else:
            self._toggleGrow()
    def _move_down(self):
        self._snake.insert(0, (self._snake[0][0], self._snake[0][1] + 1))
        if self._pending_Growth == False:
            self._snake.pop()
        else:
            self._toggleGrow()
    def _move_left(self):
        self._snake.insert(0, (self._snake[0][0] - 1, self._snake[0][1]))
        if self._pending_Growth == False:
            self._snake.pop()
        else:
            self._toggleGrow()
    def _move_right(self):
        self._snake.insert(0, (self._snake[0][0] + 1, self._snake[0][1]))
        if self._pending_Growth == False:
            self._snake.pop()
        else:
            self._toggleGrow()
