#!/usr/bin/env python3

"""Asynchronous coroutine"""
import random
import asyncio


async def async_generator():
    """Max delay set at value of 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
