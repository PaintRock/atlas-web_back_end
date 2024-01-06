#!/usr/bin/env python3

"""Import async_comprehension from the previous
file and write a measure_runtime coroutine that
will execute async_comprehension four times in
parallel using asyncio.gather."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime retuns 
    runtime"""
    s = time.perf_counter()
    func = [asyncio.create_task(async_comprehension()) for i in range(4)]
    await asyncio.gather(*funcs)
    elapsed = time.perf_counter() - s
    return elapsed
