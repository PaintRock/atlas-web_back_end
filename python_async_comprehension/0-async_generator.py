#!/usr/bin/env python3

""" Asynchronous coroutine"""
import random
import asyncio


async def async_generator():
    """Max delay set at value of 10"""
    return [i async for i in range(10)]
