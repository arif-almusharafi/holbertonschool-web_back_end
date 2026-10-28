import asyncio
import random
async def wait_random(max_delay = 10):
    x =float(random.uniform(0, max_delay))
    await asyncio.sleep(x)
    return x
