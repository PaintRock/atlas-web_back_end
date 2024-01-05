#!/usr/bin/env python3

"""A function (normal) that takes integer and returns asyncio.Task"""
import time
import asyncio


def task_wait_random(max_delay:int) -> asyncio.Task:
 """"Max delay is an int and returns asyncio.Task"""    