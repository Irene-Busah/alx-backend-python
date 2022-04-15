#!/usr/bin/env python3
"""The function return the sum of list containing integers and floating numbers"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """accepts a list mixed with integers and floating numbers"""
    return sum(mxd_lst)
