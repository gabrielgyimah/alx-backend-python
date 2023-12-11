#!/usr/bin/env python3
"""Wait Random Module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random value between 0 and max delay"""
    wait_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return wait_time
