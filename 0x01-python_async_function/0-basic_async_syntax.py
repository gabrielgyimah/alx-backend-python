#!/usr/bin/env python3
"""Wait Random Module"""

import asyncio
import random
from unittest import async_case


async def wait_random(max_delay=10):
    """Returns a random value between 0 and max delay"""
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
