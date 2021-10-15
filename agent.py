from state import State

class Agent():
    def __init__(self, state: State) -> None:
        self.state = state
        
    def get_state(self):
        return self.state.name
    
    def change_state(self, new_state: State):
        self.state = new_state
    
    def pick_value(self):
        return self.state.get_random_value()