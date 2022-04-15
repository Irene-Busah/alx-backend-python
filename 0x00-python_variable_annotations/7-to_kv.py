#!/usr/bin/env python3
"""The file returns a tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """accepts two parameters and return a tuple"""
    return k, pow(v, 2)
