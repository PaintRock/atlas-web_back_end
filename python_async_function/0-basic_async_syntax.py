#!/usr/bin/env python3

""" Asynchronous coroutine that takes an intger arg"""
import random
import asyncio


async def wait_random(max_delay=10):
    """max delay set at default value of 10"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
