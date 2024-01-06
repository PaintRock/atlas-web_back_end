#!/usr/bin/env python3

"""Asynchronous comprehensing"""
import asyncio
import random
from 0-async_generator import async_generator


async def async_comprehension():
    """Async comprehensing over async generator"""
     async_comprehension = [await async_generator() for _ in range(10)]
    return async_comprehension