import curses
class snake:
    sh = sw = snk_x = snk_y = size = 0
    snake_arr = [[0, 0]]
    w = screen = None
    
    def feed(self):
        self.size += 1
        
    #     2
    #  1      3
    #     0
    #returns -1 if game over, otherwise returns array of segment coordinates
    def move(self, direction):
        new_head = [self.snake_arr[0][0], self.snake_arr[0][1]]
        if direction == 0:
           new_head[0] += 1
        elif direction == 1:
            new_head[1] -= 2
        elif direction == 2:
            new_head[0] -= 1
        else:
            new_head[1] += 2

        if new_head[0] in [0, self.sh] or new_head[1] in [0, self.sw] or new_head in self.snake_arr[1:]:
            if new_head[0] in [0,sh]:
                print(1)
            elif new_head[1] in [0,sw]:
                print(2)
            else:
                print(3)
            return -1
        self.snake_arr.insert(0, new_head)
        if(len(self.snake_arr) > self.size):
            tail = self.snake_arr.pop()
            self.w.addch(int(tail[0]), int(tail[1]), ' ')
        return self.snake_arr
    
    
def make_snake(args): #w, sh, sw, screen
    s = snake()
    s.w, s.sh, s.sw = args
    s.snk_x = args[2]/4            #snk_x is 1/4 of the s width.
    s.snk_y = args[1]/2            #snk_y is half of the s height.
    s.snake_arr = [
        [s.snk_y, s.snk_x],
        [s.snk_y, s.snk_x-1],
        [s.snk_y, s.snk_x-2]
    ]
    s.size = 3
    return s
