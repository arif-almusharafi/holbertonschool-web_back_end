#!/usr/bin/env python3
"""Module with a coroutine that runs task_wait_random n times."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run task_wait_random n times and return delays in ascending order."""
    task = [task_wait_random(max_delay) for i in range(n)]
    results = []
    for finished in asyncio.as_completed(task):
        value = await finished
        results.append(value)
    return results
