#!/usr/bin/env python3
'''Task 1's modulefrom
'''

import asyncio
from typing import List

wait_random = __import__('1-concurrent_coroutines').wait_random

async def wait_n(n: int, max_delay: int) -> List[flaot]:

     wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
