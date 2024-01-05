#!/usr/bin/env python3

""" Asynchronous coroutine"""
import asyncio
from random import uniform
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This spawns wait_random """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
