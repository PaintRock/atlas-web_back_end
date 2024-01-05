#!/usr/bin/env python3

""" This measures the runtime"""
import time
from asyncio import run
from typing import List
wait_n = __import__('1-concurrent_corotines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
