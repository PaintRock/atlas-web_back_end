#!/usr/bin/env python3

"""Asynchronous generator"""

import random
import asyncio

async_generator = __import__('0-async_generator.py').async_generator


async def async_comprehension():
    """This is wrong becaause I have no await"""
    async_comprehension = []
    for _ in range(10):
        number = async_generator()
        async_comprehension.append(number)
    return async_comprehension
