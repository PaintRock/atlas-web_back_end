#!/usr/bin/env python3
"""Asynchronous comprehensing"""

import random
import asyncio
async_generator = __import__('0-async_generator.py').async_generator


async def async_comprehension():
    """This async function I have no await"""
     async_comprehension = [await async_generator() for _ in range(10)]
    return async_comprehension