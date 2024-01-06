#!/usr/bin/env python3

"""Function to measure the runtime
of the async comprehension """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime retuns 
    runtime"""
    s = time.time()
    func = [asyncio.create_task(async_comprehension()) for i in range(4)]
    await asyncio.gather(*funcs)
    elapsed = time.time() - s
    return elapsed
 