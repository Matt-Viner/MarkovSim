from state import State
import random

class Agent():
    def __init__(self, state: State) -> None:
        self.state = state
        
    def get_state(self):
        return self.state.name
    
    def change_state(self, new_state: State):
        self.state = new_state
    
    def pick_value(self):
        return random.choice(self.state.dist)