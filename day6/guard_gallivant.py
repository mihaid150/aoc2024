import os
from read_input import get_input


class GuardGallivant:
    def __init__(self, input_data_path: str):
        self.input_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), input_data_path))
        self.puzzle_map = get_input(input_data_path).splitlines()

        self.rows = len(self.puzzle_map)
        self.cols = len(self.puzzle_map[0])
        self.obstacles = []
        self.current_guard_position = None
        self.initial_guard_position = None
        self.initial_guard_direction = None
        self.current_direction = None
        self.guard_past_positions = set()
        self.zero_loop_positions = set()

        self.track_guard_positions = {}

    def parse_data(self) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                if self.puzzle_map[i][j] == '#':
                    self.obstacles.append((i, j))
                if self.puzzle_map[i][j] in ['^', '>', 'V', '<']:
                    self.current_guard_position = (i, j)
                    self.initial_guard_position = (i, j)
                    self.initial_guard_direction = self.puzzle_map[i][j]
                    self.current_direction = self.puzzle_map[i][j]

    def is_guard_present(self) -> bool:
        return 0 <= self.current_guard_position[0] < self.rows and 0 <= self.current_guard_position[1] < self.cols

    def add_guard_position(self) -> None:
        self.guard_past_positions.add(self.current_guard_position)

    def move_guard(self):
        gr, gc = self.current_guard_position

        # print("curr guard pos: " + str(self.current_guard_position))

        if self.current_direction == '^':
            # print("curr ^")
            if (gr - 1, gc) in self.obstacles:
                # print("next >")
                self.current_direction = '>'
            else:
                self.current_guard_position = (gr - 1, gc)
                # print("next guard pos " + str(self.current_guard_position))
        elif self.current_direction == '>':
            # print("curr >")
            if (gr, gc + 1) in self.obstacles:
                #  print("next V")
                self.current_direction = 'V'
            else:
                self.current_guard_position = (gr, gc + 1)
            # print("next guard pos " + str(self.current_guard_position))
        elif self.current_direction == 'V':
            # print("curr V")
            if (gr + 1, gc) in self.obstacles:
                #  print("next <")
                self.current_direction = '<'
            else:
                self.current_guard_position = (gr + 1, gc)
            # print("next guard pos " + str(self.current_guard_position))
        else:
            # print("curr <")
            if (gr, gc - 1) in self.obstacles:
                #  print("next ^")
                self.current_direction = '^'
            else:
                self.current_guard_position = (gr, gc - 1)
            # print("next guard pos " + str(self.current_guard_position))
        return

    def start_guard_movement(self):
        self.parse_data()

        self.add_guard_position()
        while self.is_guard_present():
            self.move_guard()

            if self.is_guard_present():
                self.add_guard_position()

        return len(list(self.guard_past_positions))

    # part 2

    def move_guard_loop(self, guard_position):
        gr, gc = guard_position

        # print("curr guard pos: " + str(self.current_guard_position))

        if self.current_direction == '^':
            # print("curr ^")
            if (gr - 1, gc) in self.obstacles:
                # print("next >")
                self.current_direction = '>'
                new_guard_position = guard_position
            else:
                new_guard_position = (gr - 1, gc)
                # print("next guard pos " + str(self.current_guard_position))
        elif self.current_direction == '>':
            # print("curr >")
            if (gr, gc + 1) in self.obstacles:
                #  print("next V")
                self.current_direction = 'V'
                new_guard_position = guard_position
            else:
                new_guard_position = (gr, gc + 1)
            # print("next guard pos " + str(self.current_guard_position))
        elif self.current_direction == 'V':
            # print("curr V")
            if (gr + 1, gc) in self.obstacles:
                #  print("next <")
                self.current_direction = '<'
                new_guard_position = guard_position
            else:
                new_guard_position = (gr + 1, gc)
            # print("next guard pos " + str(self.current_guard_position))
        else:
            # print("curr <")
            if (gr, gc - 1) in self.obstacles:
                #  print("next ^")
                self.current_direction = '^'
                new_guard_position = guard_position
            else:
                new_guard_position = (gr, gc - 1)
            # print("next guard pos " + str(self.current_guard_position))
        return new_guard_position

    def is_guard_present_loop_check(self, guard_position):
        return 0 <= guard_position[0] < self.rows and 0 <= guard_position[1] < self.cols

    def track_guard_position(self):
        if self.current_guard_position in self.track_guard_positions:
            self.track_guard_positions[self.current_guard_position] += 1
        else:
            self.track_guard_positions[self.current_guard_position] = 1

    def has_zero_in_front(self, puzzle, guard_position):
        if (self.current_direction == '^' and self.is_guard_present_loop_check(
                (guard_position[0] - 1, guard_position[1]))
                and puzzle[guard_position[0] - 1][guard_position[1]] == '0'):
            return True
        elif (self.current_direction == '>' and self.is_guard_present_loop_check(
                (guard_position[0], guard_position[1] + 1)) and
              puzzle[guard_position[0]][guard_position[1] + 1] == '0'):
            return True
        elif (self.current_direction == 'V' and self.is_guard_present_loop_check(
                (guard_position[0] + 1, guard_position[1])) and
              puzzle[guard_position[0] + 1][guard_position[1]] == '0'):
            return True
        elif (self.current_direction == '<' and self.is_guard_present_loop_check(
                (guard_position[0], guard_position[1] - 1)) and
              puzzle[guard_position[0]][guard_position[1] - 1] == '0'):
            return True
        return False

    def puzzle_contains_loop(self, puzzle):
        zero_met = 0

        test_guard_position = self.initial_guard_position
        self.current_direction = self.initial_guard_direction

        visited_states = set()

        if self.has_zero_in_front(puzzle, test_guard_position):
            zero_met += 1

        while self.is_guard_present_loop_check(test_guard_position):

            current_state = (test_guard_position, self.current_direction)

            if current_state in visited_states:
                return True
            visited_states.add(current_state)

            test_guard_position = self.move_guard_loop(test_guard_position)

            if self.has_zero_in_front(puzzle, test_guard_position):
                zero_met += 1

            if zero_met == 2:
                return True

        return False

    def count_possible_loops(self):
        self.parse_data()

        # no loops initial
        self.track_guard_position()
        while self.is_guard_present():
            self.move_guard()

            if self.is_guard_present():
                self.track_guard_position()

        self.current_guard_position = self.initial_guard_position
        self.current_direction = self.initial_guard_direction

        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for track_position in self.track_guard_positions:
            # am gasit o pozitie prin care trec de mai multe ori
            if track_position != self.initial_guard_position:
                # aici plasam in pozitie si nu in vecini un obstacol
                puzzle = self.puzzle_map.copy()
                row_as_list = list(puzzle[track_position[0]])
                row_as_list[track_position[1]] = '0'
                puzzle[track_position[0]] = ''.join(row_as_list)
                self.obstacles.append(track_position)

                if self.puzzle_contains_loop(puzzle):
                    self.zero_loop_positions.add(track_position)
                    self.current_guard_position = self.initial_guard_position

                self.obstacles.remove(track_position)
          #  print("track position " + str(track_position))
            for direction in directions:
               # print("direction " + str(direction))
                nr, nc = track_position[0] + direction[0], track_position[1] + direction[1]
               # print("obstacle at " + str(nr) + " " + str(nc))
                if (nr, nc) in self.track_guard_positions:
                    puzzle = self.puzzle_map.copy()
                    row_as_list = list(puzzle[nr])
                    row_as_list[nc] = '0'
                    puzzle[nr] = ''.join(row_as_list)
                    self.obstacles.append((nr, nc))

                    if self.puzzle_contains_loop(puzzle):
                        # print(puzzle)
                        print("found loop for " + str(nr) + " " + str(nc))
                        self.zero_loop_positions.add((nr, nc))
                        self.current_guard_position = self.initial_guard_position

                    self.obstacles.remove((nr, nc))

        return len(list(self.zero_loop_positions))
