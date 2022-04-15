#!/usr/bin/env python3
"""fixing the code"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """accepts one parameter"""
    if lst:
        return lst[0]
    else:
        return None
