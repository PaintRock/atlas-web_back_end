#!/usr/bin/env python3

""" Asynchronous coroutine"""
import asyncio
from random import uniform
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """Max delay set at value of 10"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
