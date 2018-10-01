import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def search_maze(maze, start, end):
    def isOutOfBounds(point):
        nonlocal maze
        return (point.x < 0) \
                or (point.x >= len(maze)) \
                or (point.y < 0) \
                or (point.y >= len(maze[0])) \

    def getColour(point):
        nonlocal maze
        return maze[point.x][point.y]

    def setColour(point, newColour):
        nonlocal maze
        maze[point.x][point.y] = newColour

    def getNeighbours(point):
        return [Coordinate(point.x, point.y - 1),
                Coordinate(point.x, point.y + 1),
                Coordinate(point.x - 1, point.y),
                Coordinate(point.x + 1, point.y)]

    def search_maze_helper(curr):
        nonlocal path, maze, end

        if isOutOfBounds(curr) or (getColour(curr) == BLACK):
            return False

        path.append(curr)
        setColour(curr, BLACK)
        if curr == end:
            return True

        for neighbour in getNeighbours(curr):
            if search_maze_helper(neighbour):
                return True

        # No path exists, so remove curr from path
        path.pop()
        return False

    start, end = Coordinate(*start), Coordinate(*end)
    path, visited = [], {}
    search_maze_helper(start)
    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
