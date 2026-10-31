#!/usr/bin/env python3
"""This module contains an async generator that yields random numbers."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Wait 1 second, then yield a random number between 0 and 10.

    This is repeated 10 times.
    """
    for _ in range(10):
        x = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield x
