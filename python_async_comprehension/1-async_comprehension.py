#!/usr/bin/env python3

"""Asynchronous generator"""
import asyncio
import random
from 0-async_generator import async_generator


async def async_comprehension():
    """This is wrong becaause I have no await"""
     async_comprehension = [await async_generator() for _ in range(10)]
    return async_comprehension