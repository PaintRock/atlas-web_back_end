#!/usr/bin/env python3

"""A function (normal) that takes an 
integer and returns asyncio.Task"""
import time
import asyncio


def task_wait_random(max_delay:int) -> asyncio.Task:
 """"Max delay is an int and 
 returns asyncio.Task"""
     async def wrapper():
        return await wait_random(max_delay)

    return asyncio.create_task(wrapper())
    