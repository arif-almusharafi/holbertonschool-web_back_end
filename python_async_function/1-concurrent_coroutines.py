#!/usr/bin/env python3
"""Module with a coroutine that runs wait_random n times together."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times and return the delays in ascending order."""
    task = [wait_random(max_delay) for i in range(n)]
    results = []
    for finished in asyncio.as_completed(task):
        value = await finished
        results.append(value)
    return results
