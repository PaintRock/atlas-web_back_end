#!/usr/bin/env python3
"""Asynchronous generator"""

import random
import asyncio


async def async_generator():
    """10 loops and then 10 rand"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
