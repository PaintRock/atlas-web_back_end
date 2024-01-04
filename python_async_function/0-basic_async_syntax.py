#!/usr/bin/env python3

""" Asynchronous coroutine"""
import random
import asyncio


async def wait_random(max_delay: int = 10 -> float):
    """Max delay set at value of 10"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
