#!/usr/bin/env python3
"""Write an asynchronous function sleep."""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds

    Args:
        max_delay (int, optional): value. Defaults to 10.

    Returns:
        int: value sleep
    """
    time_sleep = random.uniform(0, max_delay)
    await asyncio.sleep(time_sleep)
    return time_sleep
