#!/usr/bin/env python3

""" This measures the runtime"""
import asyncio
from asyncio import gather
from time import time
from typing import List
from random import uniform
wait_n = __import__('1-concurrent_corotines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures total exec time for wait_n"""
    start_time: = float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    total_time: float end_time - start_time
    return total_time / n
