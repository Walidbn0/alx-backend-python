#!/usr/bin/env python3
'''Task 0's module.
'''

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:

    wait_time = random.random() * max_delay
    await async.sleep(wait_time)
    return wait_time
