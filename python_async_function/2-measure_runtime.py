#!/usr/bin/env python3
"""Module that measures the average runtime of the wait_n coroutine."""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the average time per coroutine for wait_n(n, max_delay)."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return (end - start) / n
