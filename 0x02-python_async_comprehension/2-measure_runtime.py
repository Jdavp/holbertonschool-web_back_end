#!/usr/bin/env python3.7
'Run time for four parallel comprehensions'

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    'measure_runtime should measure the total runtime and return it'

    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.perf_counter()
    total_time = end_time - start_time

    return total_time
