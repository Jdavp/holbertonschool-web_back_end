#!/usr/bin/env python3
'3. Tasks'

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    'Function (not casync function, regular function syntax ) that takes an integer and returns a asyncio.Task'
    return asyncio.create_task(wait_random(max_delay))
