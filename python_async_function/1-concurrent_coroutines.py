#!/usr/bin/env python3

"""Does some stuff that I dont """
import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """This is the wait period"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """" and this is something else"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

# Test cases
print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
