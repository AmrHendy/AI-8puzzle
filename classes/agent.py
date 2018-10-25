from abc import ABC, abstractmethod
from copy import deepcopy
from state import State


class Agent(ABC):

    def __init__(self):
        # vis is set of states not arrays
        self.__vis = set()

    def expand(self, current_state, heuristic=None):
        """
            Get the child states of the current state.
        :param current_state: the current that we want to get its children, which is object of State class.
        :param heuristic: Used in cas of A* algorithm to get the heuristic cost of the child state.
        :return: list of States which is not visited yet by the search algorithm.
        """

        child_states = []

        current_arr = current_state.current
        empty_index = (current_arr.index(0) // 3, current_arr.index(0) % 3)

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for x, y in zip(dx, dy):
            if 0 <= (empty_index[0] + x) <= 2 and 0 <= (empty_index[1] + y) <= 2:
                new_arr = deepcopy(current_state.current)
                old_index = new_arr.index(0)
                new_index = (empty_index[0] + x) * 3 + (empty_index[1] + y)
                new_arr[old_index], new_arr[new_index] = new_arr[new_index], new_arr[old_index]
                child_state = State(new_arr, current_state, heuristic)
                if child_state not in self.vis:
                    child_states.append(child_state)

        return child_states

    def get_steps(self, final_state):
        """
            Get the path from that final state to the first given state by the user.
        :param final_state: final state reached, aka goal state.
        :return: list of State objects of the path, in reversed order, first of the list is the last state and so on.
        """
        steps = []
        while final_state is not None:
            steps.append(deepcopy(final_state))
            final_state = final_state.parent
        return steps

    @property
    def vis(self):
        """
            Getter for the visited set.
        :return: set of State object.
        """
        return self.__vis

    @abstractmethod
    def search(self, initial_state):
        """
            Abstract method for search, will be used in BFS, DFS, and A* algorithms.
        :param initial_state: initial state of the puzzle given by the user.
        :return: list of state that describe the path.
        """
        pass

