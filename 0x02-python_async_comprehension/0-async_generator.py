#!/usr/bin/env python3
""" Async Generator Module """
import asyncio
import random


async def async_generator():
    """Generates random numbers every second"""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
