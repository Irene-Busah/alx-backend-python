#!/usr/bin/env python3
"""The function returns a function that multiply a float by a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """accepts a floating number as parameter"""
    def myFunction(multiply: float) -> float:
        """creating the multiply"""
        return float(multiply * multiplier)
    return myFunction
