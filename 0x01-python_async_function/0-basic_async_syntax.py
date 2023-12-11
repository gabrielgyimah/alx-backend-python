#!/usr/bin/env python3
"""Wait Random Module"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    """Returns a random value between 0 and max delay"""
    value: Union[int, float] = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
