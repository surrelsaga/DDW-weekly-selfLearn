# State space search

# Nodes will be the states

# Edges will be labelled with a number representing a an input to 
# make a state transition

def goal_test(state):
    return state == 'G'

statemap = {'S': ['A', 'B'],
            'A': ['S', 'C', 'D'],
            'B': ['S', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['A', 'B', 'F', 'H'],
            'E': ['B', 'H'],
            'F': ['C', 'D', 'G'],
            'G': ['F', 'H'],
            'H': ['D', 'E', 'G']}

# e.g: of using an action to transit the state
# e.g: action 0 -> transit from state D to state A

# statemap['D'][0] # returns state A
# statemap['D'][1] # returns state B
# statemap['D'][2] # returns state F
# statemap['D'][3] # returns state H

def statemap_successor(state, action):
    return statemap[state][action]


# OOP implementation

# State machine class
from abc import ABC, abstractmethod

class StateMachine(ABC):
    # this method set the state Attribute using the value in start_state
    def start(self) -> None:
        self.state = self.start_state

    def step(self, inp: Any) -> Any:
        next_state, current_output = self.get_next_values(self.state, inp)
        self.state = next_state
        
        return current_output
        
        
    def transduce(self, inp_list: Sequence[Any]) -> list[Any]:
        output_list = []
        self.start()
        
        for inp in inp_list:
            if self.is_done():
                break
            current_output = self.step(inp)
            output_list.append(current_output)
        
        return output_list

    @property
    @abstractmethod
    def start_state(self) -> Any:
        pass 

    @abstractmethod
    def get_next_values(self, state: Any, inp: Any) -> tuple[Any, Any]:
        pass

    def done(self, state: Any) -> bool:
        return False

    def is_done(self) -> bool:
        return self.done(self.state)


# State space search
class StateSpaceSearch(StateMachine):
    @property
    @abstractmethod
    def statemap(self):
        pass

    @property
    @abstractmethod
    def legal_inputs(self):
        pass

    @property
    @abstractmethod
    def start_state(self):
        return self.__start_state

    @start_state.setter
    @abstractmethod
    def start_state(self, value):
        self.__start_state = value

# This is the class for the map
class MapSM(StateSpaceSearch):

    def __init__(self, start):
        self.start_state = start

    @property
    def statemap(self):
        # tuple represents (next_state, output)
        statemap = {"S": [("A", "A"), ("B", "B")],
                    "A": [("S", "S"), ("C", "C"), ("D", "D")],
                    "B": [("S", "S"), ("D", "D"), ("E", "E")],
                    "C": [("A", "A"), ("F", "F")],
                    "D": [("A", "A"), ("B", "B"), ("F", "F"), ("H", "H")],
                    "E": [("B", "B"), ("H", "H")],
                    "F": [("C", "C"), ("D", "D"), ("G", "G")],
                    "H": [("D", "D"), ("E", "E"), ("G", "G")],
                    "G": [("F", "F"), ("H", "H")]}
        return statemap
