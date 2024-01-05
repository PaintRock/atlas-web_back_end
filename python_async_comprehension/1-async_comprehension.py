#!/usr/bin/env python3

"""Asynchronous generator"""

import random
import asyncio

async_generator = __import__('0-async_generator.py').async_generator


async def async_comprehension():
    """10 loops and then 10 rand"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
