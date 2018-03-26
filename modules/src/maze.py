import config
import modules
from templates.text import TextTemplate

from random import randint

def strmaze(grid):
    unichr_nums = [
        32,
        9590,
        9591,
        9581,
        9588,
        9472,
        9582,
        9516,
        9589,
        9584,
        9474,
        9500,
        9583,
        9524,
        9508,
        9532,
    ]
    
    characters = [unichr(unichr_num) for unichr_num in unichr_nums]
    
    size = len(grid)
    s = ''
    for y in xrange(size+1):
        for x in xrange(size+1):
            
            unichr_num = 0
            if 0 <= x-1 < size and 0 <= y-1 < size:
                if not grid[x-1][y-1] & 1:
                    unichr_num = unichr_num | 8
                if not grid[x-1][y-1] & 2:
                    unichr_num = unichr_num | 4
            if 0 <= x-1 < size and 0 <= y < size:
                if not grid[x-1][y] & 1:
                    unichr_num = unichr_num | 2
                if not grid[x-1][y] & 8:
                    unichr_num = unichr_num | 4
            if 0 <= x < size and 0 <= y-1 < size:
                if not grid[x][y-1] & 4:
                    unichr_num = unichr_num | 8
                if not grid[x][y-1] & 2:
                    unichr_num = unichr_num | 1
            if 0 <= x < size and 0 <= y < size:
                if not grid[x][y] & 4:
                    unichr_num = unichr_num | 2
                if not grid[x][y] & 8:
                    unichr_num = unichr_num | 1
                    
            s += characters[unichr_num]
            if unichr_num & 1:
                s += characters[5]
            else:
                s += ' '
                
        s += '\n'
        
    return s[:-1]

def maze(size):
    size = int(size)
    
    if not 0 < size <= 20:
        return 'Please enter a size between 1 and 20'
    
    directions = {1: (1, 0), 2: (0, 1), 4: (-1, 0), 8: (0, -1)}
    anti_directions = {1: 4, 2: 8, 4: 1, 8: 2}
    grid = [[0 for y in xrange(size)] for x in xrange(size)]
    reserve_start = (0, 0)
    
    reserve_queue = [(None, reserve_start)]
    while len(reserve_queue) > 0:
        from_direction_int, active_start = reserve_queue.pop(randint(0, len(reserve_queue) - 1))
        active_start_x, active_start_y = active_start
        
        if grid[active_start_x][active_start_y] == 0:
            
            if from_direction_int:
                from_direction_x, from_direction_y = directions[from_direction_int]
                origin_x = active_start_x - from_direction_x
                origin_y = active_start_y - from_direction_y
                grid[origin_x][origin_y] += from_direction_int
                grid[active_start_x][active_start_y] += anti_directions[from_direction_int]

            active_queue = [active_start]
            while len(active_queue) > 0:
                cell_x, cell_y = active_queue.pop(randint(0, len(active_queue) - 1))

                for direction_int in directions:
                    direction_x, direction_y = directions[direction_int]
                    adjacent_x = cell_x + direction_x
                    adjacent_y = cell_y + direction_y

                    if 0 <= adjacent_x < size and 0 <= adjacent_y < size:

                        if grid[adjacent_x][adjacent_y] == 0:
                            if randint(0, 1):

                                reserve_queue += [(direction_int, (adjacent_x, adjacent_y))]

                            else:
                                
                                grid[cell_x][cell_y] += direction_int
                                grid[adjacent_x][adjacent_y] += anti_directions[direction_int]
                                active_queue += [(adjacent_x, adjacent_y)]
                                
    grid[0][randint(0, size - 1)] += 4
    grid[size - 1][randint(0, size - 1)] += 1
    
    return strmaze(grid)

def process(input, entities=None):
    output = {}
    try:
        
        assert('size' in entities)
        text_i_want_returned = maze(entities['size'][0]['value'])
        
        message = TextTemplate(text_i_want_returned).get_message()
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output
