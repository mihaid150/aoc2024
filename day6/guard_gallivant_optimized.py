import os
from collections import defaultdict

# Direction handling
DIRECTIONS = ['^', '>', 'V', '<']
DIR_VECTORS = {
    '^': (-1, 0),
    'V': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}


def turn_right(direction):
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def get_input(input_data_path):
    with open(input_data_path, 'r') as f:
        return f.read()


class GuardGallivantOptimized:
    def __init__(self, input_data_path: str):
        self.input_data_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), input_data_path)
        )
        self.puzzle_map = get_input(self.input_data_path).splitlines()
        self.rows = len(self.puzzle_map)
        self.cols = len(self.puzzle_map[0]) if self.rows > 0 else 0

        self.obstacles = set()
        self.initial_guard_position = None
        self.initial_guard_direction = None
        self.current_direction = None

        self.transitions = {}
        self.guard_path_positions = set()  # Positions visited by guard in part 1

        self.parse_data()
        # First, run part 1 logic to find guard path and visited positions
        self.run_initial_guard_movement()

        # After part 1, build transitions for the graph approach for part 2
        self.build_transitions()

    def parse_data(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.puzzle_map[i][j]
                if cell == '#':
                    self.obstacles.add((i, j))
                elif cell in DIRECTIONS:
                    self.initial_guard_position = (i, j)
                    self.initial_guard_direction = cell
                    self.current_direction = cell

    def in_bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_blocked(self, r, c):
        return (r, c) in self.obstacles or not self.in_bounds(r, c)

    def next_state(self, r, c, d):
        """Compute the next state from (r, c, d) given current obstacles."""
        dr, dc = DIR_VECTORS[d]
        nr, nc = r + dr, c + dc
        if self.is_blocked(nr, nc):
            # turn right
            nd = turn_right(d)
            return (r, c, nd)
        else:
            # move forward
            return (nr, nc, d)

    def build_transitions(self):
        """
        Build a transitions dictionary for all in-bound cells and directions.
        This allows quick cycle detection and updates.
        """
        for r in range(self.rows):
            for c in range(self.cols):
                for d in DIRECTIONS:
                    self.transitions[(r, c, d)] = self.next_state(r, c, d)

    def update_transitions_for_cell(self, r, c):
        """
        When adding/removing an obstacle at (r, c), only transitions for states
        that move into or start in (r,c) might change. Update transitions locally.
        """
        candidates = [(r, c)]
        # Also consider cells that could lead into (r,c)
        for d, (dr, dc) in DIR_VECTORS.items():
            rr = r - dr
            cc = c - dc
            if self.in_bounds(rr, cc):
                candidates.append((rr, cc))

        for (rr, cc) in candidates:
            if self.in_bounds(rr, cc):
                for d in DIRECTIONS:
                    self.transitions[(rr, cc, d)] = self.next_state(rr, cc, d)

    def run_initial_guard_movement(self):
        """
        Part 1 logic: simulate the guard's path to find all distinct visited cells.
        No obstacles are added here. Just follow the rules until guard leaves the map.
        """
        r, c = self.initial_guard_position
        d = self.initial_guard_direction

        visited_positions = set()
        visited_positions.add((r, c))

        while True:
            dr, dc = DIR_VECTORS[d]
            nr, nc = r + dr, c + dc
            if self.is_blocked(nr, nc):
                # turn right
                d = turn_right(d)
            else:
                r, c = nr, nc
                if not self.in_bounds(r, c):
                    # Guard leaves the map
                    break
                visited_positions.add((r, c))

        self.guard_path_positions = visited_positions

    def cycle_detection(self):
        """
        From the initial guard state, detect if there's a cycle in the transitions.
        """
        start_state = (self.initial_guard_position[0], self.initial_guard_position[1], self.initial_guard_direction)
        visited = set()
        in_stack = set()

        def dfs(state):
            if state not in visited:
                visited.add(state)
                in_stack.add(state)
                next_s = self.transitions.get(state)
                if next_s and self.in_bounds(next_s[0], next_s[1]):
                    if next_s in in_stack:
                        # cycle found
                        return True
                    if dfs(next_s):
                        return True
                in_stack.remove(state)
            return False

        return dfs(start_state)

    def test_obstacle_for_loop(self, r, c):
        """
        Temporarily add an obstacle at (r, c) and check if a loop occurs.
        """
        # Can't place an obstacle at the guard's initial position
        if (r, c) == self.initial_guard_position:
            return False
        # Already an obstacle?
        if (r, c) in self.obstacles:
            return False

        self.obstacles.add((r, c))
        self.update_transitions_for_cell(r, c)

        has_cycle = self.cycle_detection()

        # Remove obstacle
        self.obstacles.remove((r, c))
        self.update_transitions_for_cell(r, c)

        return has_cycle

    def find_loop_positions(self):
        """
        Find all positions where placing a single obstacle creates a loop.

        Strategy:
        - Consider cells in the guard path or around it.
          In the example solution, they considered cells through which guard passes more than once
          and their neighbors. Here, we'll consider:
          - All visited cells (except initial and those already obstacles)
          - Their neighbors
        """
        candidate_positions = set()
        # Add all visited positions and their neighbors as candidates
        for (r, c) in self.guard_path_positions:
            # check cell itself
            if (r, c) != self.initial_guard_position and (r, c) not in self.obstacles:
                candidate_positions.add((r, c))
            # check neighbors
            for dr, dc in DIR_VECTORS.values():
                nr, nc = r + dr, c + dc
                if self.in_bounds(nr, nc):
                    if (nr, nc) != self.initial_guard_position and (nr, nc) not in self.obstacles:
                        candidate_positions.add((nr, nc))

        loop_positions = []
        for (r, c) in candidate_positions:
            if self.test_obstacle_for_loop(r, c):
                print("found loop for " + str(r) + " " + str(c))
                loop_positions.append((r, c))

        return len(loop_positions)
