#!/usr/bin/env python3
'2. Measure the runtime'

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    'Function that measures the total execution time, function should return a float. Use time module to measure an approximate elapsed time.'

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    time_for_each_random_integer = total_time / n

    return time_for_each_random_integer
