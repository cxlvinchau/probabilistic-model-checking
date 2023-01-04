from typing import Tuple, Any, Dict, Set

import numpy as np

class State:
    """State of a DTMC"""

    def __init__(self, id, name=None, ap=[]):
        self.id = id
        self.name = name if name else f"s{id}"
        self.ap = ap

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        if isinstance(other, State):
            return other.id == self.id
        return False

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"State({self.id}, name={self.name}, ap={self.ap})"